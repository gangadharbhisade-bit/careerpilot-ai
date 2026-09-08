from fastapi import APIRouter
from app.schemas.schemas import SkillGapInput, SkillGapResponse
from app.services.skill_gap_engine import analyze_skill_gap

router = APIRouter(prefix="/skill-gap", tags=["Skill Gap"])

@router.post("/analyze", response_model=SkillGapResponse)
def analyze(gap_input: SkillGapInput):
    return analyze_skill_gap(gap_input.current_skills, gap_input.target_role)
