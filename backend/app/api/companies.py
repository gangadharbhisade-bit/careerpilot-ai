from fastapi import APIRouter
from app.services.job_company_service import get_target_companies

router = APIRouter(prefix="/companies", tags=["Target Companies"])

@router.get("/target")
def target_companies(career: str = "AI Engineer"):
    return {
        "career": career,
        "companies": get_target_companies(career)
    }
