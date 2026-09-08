from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.entities import User, InterviewSession
from app.schemas.schemas import InterviewStartInput, InterviewAnswerInput, InterviewTurnResponse
from app.services.interview_engine import get_next_question, evaluate_answer
from app.api.auth import get_current_user

router = APIRouter(prefix="/interview", tags=["Mock Interview"])

@router.post("/start", response_model=InterviewTurnResponse)
def start_interview(
    start_in: InterviewStartInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = InterviewSession(
        user_id=current_user.id,
        target_role=start_in.target_role,
        interview_type=start_in.interview_type,
        status="in_progress",
        questions_history=[]
    )
    db.add(session)
    db.commit()
    db.refresh(session)

    first_q = get_next_question(start_in.target_role, start_in.interview_type, 0)
    
    return {
        "session_id": session.id,
        "question_number": 1,
        "question": first_q,
        "previous_evaluation": None,
        "is_finished": False,
        "final_summary": None
    }

@router.post("/answer", response_model=InterviewTurnResponse)
def submit_answer(
    answer_in: InterviewAnswerInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    session = db.query(InterviewSession).filter(
        InterviewSession.id == answer_in.session_id,
        InterviewSession.user_id == current_user.id
    ).first()

    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found")

    history = session.questions_history or []
    current_q_idx = len(history)
    current_q = get_next_question(session.target_role, session.interview_type, current_q_idx)

    # Evaluate answer
    eval_result = evaluate_answer(current_q, answer_in.user_answer)
    
    history.append({
        "question": current_q,
        "user_answer": answer_in.user_answer,
        "score": eval_result["score"],
        "strengths": eval_result["strengths"],
        "weaknesses": eval_result["weaknesses"],
        "suggested_answer": eval_result["improved_answer_sample"]
    })
    
    session.questions_history = history
    db.commit()

    next_q_idx = len(history)
    next_q = get_next_question(session.target_role, session.interview_type, next_q_idx)
    
    is_finished = next_q_idx >= 3 or "Thank you!" in next_q

    final_summary = None
    if is_finished:
        session.status = "completed"
        scores = [h["score"] for h in history]
        avg_score = round(sum(scores) / len(scores), 1) if scores else 7.0
        session.overall_score = avg_score
        session.overall_feedback = f"Completed {len(history)} questions with an average score of {avg_score}/10."
        db.commit()

        final_summary = {
            "overall_score": avg_score,
            "total_questions": len(history),
            "summary_feedback": session.overall_feedback,
            "questions_summary": history
        }

    return {
        "session_id": session.id,
        "question_number": next_q_idx + 1,
        "question": next_q if not is_finished else "Interview Completed!",
        "previous_evaluation": eval_result,
        "is_finished": is_finished,
        "final_summary": final_summary
    }
