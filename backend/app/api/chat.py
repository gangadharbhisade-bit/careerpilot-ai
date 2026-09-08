from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.entities import User, ChatSession, ChatMessage, UserProfile
from app.schemas.schemas import ChatMessageInput, ChatResponse
from app.services.ai_service import AIService
from app.api.auth import get_current_user

router = APIRouter(prefix="/chat", tags=["Chatbot"])

@router.post("", response_model=ChatResponse)
async def chat_message(
    chat_input: ChatMessageInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Get active session or create new
    session_id = chat_input.session_id
    if session_id:
        session = db.query(ChatSession).filter(ChatSession.id == session_id, ChatSession.user_id == current_user.id).first()
    else:
        session = ChatSession(user_id=current_user.id, title=chat_input.message[:30] + "...")
        db.add(session)
        db.commit()
        db.refresh(session)
        session_id = session.id

    # Retrieve recent session history (last 6 messages) BEFORE saving current prompt
    recent_messages = db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).order_by(ChatMessage.created_at.asc()).all()
    
    history_list = [{"sender": m.sender, "content": m.content} for m in recent_messages[-6:]]

    # Save user message
    user_msg = ChatMessage(session_id=session_id, sender="user", content=chat_input.message)
    db.add(user_msg)

    # Get user profile context
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    profile_dict = profile.__dict__ if profile else {}

    # Query AI Service with conversation history
    ai_result = await AIService.chat(user_input := chat_input.message, profile_dict, history_list)

    # Save AI response
    ai_msg = ChatMessage(
        session_id=session_id,
        sender="assistant",
        content=ai_result["reply"],
        structured_payload=ai_result.get("structured_payload")
    )
    db.add(ai_msg)
    db.commit()

    return {
        "session_id": session_id,
        "reply": ai_result["reply"],
        "structured_payload": ai_result.get("structured_payload"),
        "is_demo_mode": ai_result.get("is_demo_mode", True)
    }

@router.get("/history")
def get_chat_history(
    session_id: int = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if session_id:
        session = db.query(ChatSession).filter(ChatSession.id == session_id, ChatSession.user_id == current_user.id).first()
        if not session:
            raise HTTPException(status_code=404, detail="Chat session not found or unauthorized")
        messages = db.query(ChatMessage).filter(ChatMessage.session_id == session.id).order_by(ChatMessage.created_at.asc()).all()
        return [{"id": m.id, "sender": m.sender, "content": m.content, "structured_payload": m.structured_payload} for m in messages]
    
    sessions = db.query(ChatSession).filter(ChatSession.user_id == current_user.id).order_by(ChatSession.created_at.desc()).all()
    return [{"id": s.id, "title": s.title, "created_at": s.created_at} for s in sessions]

@router.delete("/clear")
def clear_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    db.query(ChatSession).filter(ChatSession.user_id == current_user.id).delete()
    db.commit()
    return {"status": "cleared"}
