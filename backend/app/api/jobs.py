from fastapi import APIRouter
from app.services.job_company_service import get_job_platforms, get_scam_warnings

router = APIRouter(prefix="/jobs", tags=["Jobs & Internships"])

@router.get("")
def get_jobs_guidance():
    return {
        "platforms": get_job_platforms(),
        "scam_warnings": get_scam_warnings()
    }
