from fastapi import APIRouter
from app.schemas.schemas import ResumeInput, ResumeResponse
from app.services.resume_engine import analyze_resume

router = APIRouter(prefix="/resume", tags=["Resume Assistant"])

@router.post("/analyze", response_model=ResumeResponse)
def analyze_resume_text(resume_input: ResumeInput):
    return analyze_resume(resume_input.resume_text, resume_input.target_role)
