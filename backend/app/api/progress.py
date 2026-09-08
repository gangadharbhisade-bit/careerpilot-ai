from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.entities import User, DailyTask, UserProfile, InterviewSession
from app.schemas.schemas import TaskToggleInput, TaskCreateInput
from app.api.auth import get_current_user
from app.services.skill_gap_engine import get_required_skills_for_role, normalize_skill
from datetime import datetime

router = APIRouter(prefix="/progress", tags=["Progress & Daily Planner"])

CAREER_DEFAULT_TASKS = {
    "Android Developer": [
        {"text": "Study Kotlin OOP, Interfaces & Null Safety", "topic": "Kotlin", "mins": 45},
        {"text": "Build a responsive Jetpack Compose Layout UI card", "topic": "Android UI", "mins": 45},
        {"text": "Fetch REST API data using Retrofit & Coroutines", "topic": "Networking", "mins": 60},
        {"text": "Implement Room DB local storage for offline notes", "topic": "Database", "mins": 60}
    ],
    "Data Analyst": [
        {"text": "Master XLOOKUP & Pivot Charts in Excel", "topic": "Excel", "mins": 45},
        {"text": "Solve 5 SQL GROUP BY & JOIN query problems", "topic": "SQL", "mins": 45},
        {"text": "Clean a messy CSV dataset using Pandas DataFrames", "topic": "Python", "mins": 60},
        {"text": "Create an interactive sales KPI dashboard in Power BI", "topic": "Power BI", "mins": 60}
    ],
    "Cybersecurity Engineer": [
        {"text": "Analyze network packets in Wireshark", "topic": "Networking", "mins": 45},
        {"text": "Practice Linux CLI file permissions & process commands", "topic": "Linux", "mins": 45},
        {"text": "Complete OWASP SQL Injection lab on PortSwigger", "topic": "Web Security", "mins": 60},
        {"text": "Configure Splunk dashboard to monitor failed logins", "topic": "SIEM", "mins": 60}
    ],
    "Frontend Developer": [
        {"text": "Build an accessible Semantic HTML5 & CSS Flexbox layout", "topic": "HTML/CSS", "mins": 45},
        {"text": "Solve 3 JavaScript ES6 Async/Await coding exercises", "topic": "JavaScript", "mins": 45},
        {"text": "Create custom auto-saving form hook in React 18", "topic": "React", "mins": 60},
        {"text": "Migrate React project components to TypeScript interfaces", "topic": "TypeScript", "mins": 60}
    ],
    "AI Engineer": [
        {"text": "Implement Gradient Descent & Matrix math in NumPy", "topic": "Math for AI", "mins": 45},
        {"text": "Train a Decision Tree model with Scikit-Learn", "topic": "Machine Learning", "mins": 45},
        {"text": "Build a Deep Neural Net in PyTorch for digit classification", "topic": "Deep Learning", "mins": 60},
        {"text": "Create a RAG pipeline over custom PDFs using LangChain", "topic": "LLMs & RAG", "mins": 60}
    ]
}

DEFAULT_FALLBACK_TASKS = [
    {"text": "Complete core technology fundamentals module", "topic": "Core Fundamentals", "mins": 45},
    {"text": "Solve 2 LeetCode / Algorithmic coding challenges", "topic": "Algorithms", "mins": 45},
    {"text": "Implement mini-project component and push to GitHub", "topic": "Projects", "mins": 60},
    {"text": "Review technical interview questions for your target career", "topic": "Interview Prep", "mins": 30}
]

@router.get("")
def get_progress(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    target_career = profile.target_career if profile else None
    user_skills = profile.skills if (profile and profile.skills) else []
    today_str = datetime.now().strftime("%Y-%m-%d")

    # 1. Fetch User Tasks
    tasks = db.query(DailyTask).filter(DailyTask.user_id == current_user.id).order_by(DailyTask.created_at.desc()).all()

    # If user has a target career set but no tasks, populate initial career-specific tasks
    if not tasks and target_career:
        task_templates = CAREER_DEFAULT_TASKS.get(target_career, DEFAULT_FALLBACK_TASKS)
        new_tasks = []
        for template in task_templates:
            new_tasks.append(
                DailyTask(
                    user_id=current_user.id,
                    task_text=template["text"],
                    topic=template["topic"],
                    estimated_minutes=template["mins"],
                    completed=False,
                    date_str=today_str
                )
            )
        for t in new_tasks:
            db.add(t)
        db.commit()
        tasks = db.query(DailyTask).filter(DailyTask.user_id == current_user.id).order_by(DailyTask.created_at.desc()).all()

    total_tasks = len(tasks)
    completed_count = sum(1 for t in tasks if t.completed)
    completion_percentage = round((completed_count / total_tasks) * 100, 1) if total_tasks > 0 else 0.0

    # 2. Interview Readiness Score
    completed_interviews = db.query(InterviewSession).filter(
        InterviewSession.user_id == current_user.id,
        InterviewSession.status == "completed"
    ).all()

    if completed_interviews:
        scores = [i.overall_score for i in completed_interviews if i.overall_score is not None]
        avg_score = sum(scores) / len(scores) if scores else 7.0
        interview_readiness_score = min(100, int(avg_score * 10))
    else:
        interview_readiness_score = 0

    # 3. Resume Readiness & Skills Progress
    if target_career:
        required_skills = get_required_skills_for_role(target_career)
        norm_user_skills = [normalize_skill(s).lower() for s in user_skills]

        mastered_skills = [s for s in user_skills]
        pending_skills = []

        matched_count = 0
        for req in required_skills:
            req_clean = req.lower()
            if any(u in req_clean or req_clean in u for u in norm_user_skills):
                matched_count += 1
            else:
                pending_skills.append(req)

        resume_readiness_score = int((matched_count / len(required_skills)) * 100) if required_skills else 0
    else:
        mastered_skills = user_skills
        pending_skills = []
        resume_readiness_score = 0
        required_skills = []

    # 4. Overall Readiness Score Calculation
    if not target_career:
        overall_readiness_score = 0
    else:
        # Profile completeness factor (up to 25)
        profile_completeness = 0
        if profile.career_goal: profile_completeness += 10
        if profile.skills: profile_completeness += 10
        if profile.experience_level: profile_completeness += 5

        # Skill match factor (up to 50)
        skill_factor = (matched_count / len(required_skills)) * 50 if required_skills else 0

        # Task completion factor (up to 25)
        task_factor = (completion_percentage / 100.0) * 25

        overall_readiness_score = min(100, int(profile_completeness + skill_factor + task_factor))

    return {
        "overall_readiness_score": overall_readiness_score,
        "completed_skills": mastered_skills,
        "pending_skills": pending_skills,
        "completed_projects_count": len(profile.current_projects) if (profile and profile.current_projects) else 0,
        "interview_readiness_score": interview_readiness_score,
        "resume_readiness_score": resume_readiness_score,
        "daily_planner": {
            "total_tasks": total_tasks,
            "completed_tasks": completed_count,
            "completion_percentage": completion_percentage,
            "tasks": [{"id": t.id, "task_text": t.task_text, "topic": t.topic, "estimated_minutes": t.estimated_minutes, "completed": t.completed, "date_str": t.date_str} for t in tasks]
        }
    }

@router.post("/task/toggle")
def toggle_task(
    input_data: TaskToggleInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(DailyTask).filter(DailyTask.id == input_data.task_id, DailyTask.user_id == current_user.id).first()
    if task:
        task.completed = input_data.completed
        db.commit()
        return {"status": "updated", "task_id": task.id, "completed": task.completed}
    return {"status": "not_found"}

@router.post("/task/create")
def create_task(
    input_data: TaskCreateInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = DailyTask(
        user_id=current_user.id,
        task_text=input_data.task_text,
        topic=input_data.topic,
        estimated_minutes=input_data.estimated_minutes,
        date_str=input_data.date_str,
        completed=False
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"id": task.id, "task_text": task.task_text, "completed": False}
