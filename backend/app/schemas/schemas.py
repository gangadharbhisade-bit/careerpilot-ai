from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Any, Dict
from datetime import datetime

# --- AUTH SCHEMAS ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    full_name: Optional[str] = "Career Navigator"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Dict[str, Any]

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# --- PROFILE SCHEMAS ---
class ProfileSchema(BaseModel):
    education: Optional[str] = None
    degree: Optional[str] = None
    branch: Optional[str] = None
    current_role: Optional[str] = None
    experience_level: Optional[str] = "Beginner"
    skills: List[str] = []
    programming_languages: List[str] = []
    interests: List[str] = []
    target_career: Optional[str] = None
    target_industry: Optional[str] = "Technology"
    preferred_location: Optional[str] = "Remote"
    remote_preference: Optional[str] = "Remote"
    salary_expectation: Optional[str] = None
    available_learning_time: Optional[str] = "2 hours/day"
    career_goal: Optional[str] = None
    current_projects: List[str] = []
    certifications: List[str] = []

    class Config:
        from_attributes = True


# --- CHAT SCHEMAS ---
class ChatMessageInput(BaseModel):
    message: str = Field(..., min_length=1)
    session_id: Optional[int] = None

class StructuredPayload(BaseModel):
    goal: Optional[str] = None
    level: Optional[str] = None
    skills_to_learn: Optional[List[str]] = None
    roadmap_overview: Optional[List[Dict[str, Any]]] = None
    resources: Optional[Dict[str, List[Dict[str, str]]]] = None
    projects: Optional[List[Dict[str, Any]]] = None
    application_channels: Optional[List[Dict[str, str]]] = None
    interview_prep: Optional[List[str]] = None
    next_steps: Optional[List[str]] = None

class ChatResponse(BaseModel):
    session_id: int
    reply: str
    structured_payload: Optional[Dict[str, Any]] = None
    is_demo_mode: bool = False


# --- ROADMAP SCHEMAS ---
class RoadmapRequest(BaseModel):
    target_career: str = "AI Engineer"
    duration: str = "6-month" # 30-day, 3-month, 6-month, 1-year
    level: str = "Beginner"   # Beginner, Intermediate, Advanced

class WeeklyPlan(BaseModel):
    week: int
    title: str
    topics: List[str]
    practice: str

class PhasePlan(BaseModel):
    phase_number: int
    phase_title: str
    duration_weeks: int
    skills_covered: List[str]
    weekly_breakdown: List[WeeklyPlan]
    milestone_project: str
    learning_resources: List[Dict[str, str]]

class RoadmapResponse(BaseModel):
    target_career: str
    duration: str
    level: str
    overview: str
    phases: List[PhasePlan]


# --- SKILL GAP SCHEMAS ---
class SkillGapInput(BaseModel):
    current_skills: List[str]
    target_role: str

class SkillGapResponse(BaseModel):
    target_role: str
    current_skills: List[str]
    required_skills: List[str]
    missing_skills: List[str]
    readiness_percentage: float
    priority_order: List[Dict[str, Any]] # {skill, priority, estimated_hours, learning_resource}


# --- RESUME ANALYSIS SCHEMAS ---
class ResumeInput(BaseModel):
    target_role: str
    resume_text: str

class ResumeResponse(BaseModel):
    ats_score: int
    matched_keywords: List[str]
    missing_keywords: List[str]
    strengths: List[str]
    improvements: List[str]
    suggested_bullet_points: List[Dict[str, str]] # {original, improved}
    actionable_next_steps: List[str]


# --- INTERVIEW SCHEMAS ---
class InterviewStartInput(BaseModel):
    target_role: str = "Software Developer"
    interview_type: str = "Technical" # HR, Technical, Coding, Behavioral, System Design

class InterviewAnswerInput(BaseModel):
    session_id: int
    user_answer: str

class QuestionEvaluation(BaseModel):
    score: float # 1 to 10
    strengths: List[str]
    weaknesses: List[str]
    improved_answer_sample: str

class InterviewTurnResponse(BaseModel):
    session_id: int
    question_number: int
    question: str
    previous_evaluation: Optional[QuestionEvaluation] = None
    is_finished: bool = False
    final_summary: Optional[Dict[str, Any]] = None


# --- CAREER COMPARISON SCHEMAS ---
class CompareRequest(BaseModel):
    career_a: str = "Data Scientist"
    career_b: str = "AI Engineer"

class CareerMetric(BaseModel):
    metric_name: str
    career_a_value: str
    career_b_value: str

class CompareResponse(BaseModel):
    career_a: str
    career_b: str
    summary: str
    comparison_table: List[CareerMetric]
    verdict_guidance: str


# --- PROGRESS SCHEMAS ---
class TaskToggleInput(BaseModel):
    task_id: int
    completed: bool

class TaskCreateInput(BaseModel):
    task_text: str
    topic: Optional[str] = "Learning"
    estimated_minutes: int = 30
    date_str: str
