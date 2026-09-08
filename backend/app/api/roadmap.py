from fastapi import APIRouter
from app.schemas.schemas import RoadmapRequest, RoadmapResponse
from app.services.roadmap_engine import generate_roadmap

router = APIRouter(prefix="/roadmap", tags=["Roadmap"])

@router.post("/generate", response_model=RoadmapResponse)
def create_roadmap(req: RoadmapRequest):
    data = generate_roadmap(
        target_career=req.target_career,
        duration=req.duration,
        level=req.level
    )
    # Ensure returned career matches requested career
    data["target_career"] = req.target_career
    return data
