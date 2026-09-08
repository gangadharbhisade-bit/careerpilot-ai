from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.database import engine, Base
from app.core.rate_limiter import RateLimiterMiddleware
from app.core.logger import logger

# Import API Routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.chat import router as chat_router
from app.api.roadmap import router as roadmap_router
from app.api.skill_gap import router as skill_gap_router
from app.api.resources import router as resources_router
from app.api.jobs import router as jobs_router
from app.api.companies import router as companies_router
from app.api.resume import router as resume_router
from app.api.interview import router as interview_router
from app.api.comparison import router as comparison_router
from app.api.progress import router as progress_router

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS Middleware with Vercel deployment support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.ENVIRONMENT == "development" else settings.ALLOWED_ORIGINS,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting Middleware (100 req/min)
app.add_middleware(RateLimiterMiddleware, max_requests=120, window_seconds=60)

# Global Security & Exception Handler (No stack trace exposure)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Runtime Error on {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Something went wrong processing your request. Please try again."}
    )

# Include Routers
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(profile_router, prefix=settings.API_V1_STR)
app.include_router(chat_router, prefix=settings.API_V1_STR)
app.include_router(roadmap_router, prefix=settings.API_V1_STR)
app.include_router(skill_gap_router, prefix=settings.API_V1_STR)
app.include_router(resources_router, prefix=settings.API_V1_STR)
app.include_router(jobs_router, prefix=settings.API_V1_STR)
app.include_router(companies_router, prefix=settings.API_V1_STR)
app.include_router(resume_router, prefix=settings.API_V1_STR)
app.include_router(interview_router, prefix=settings.API_V1_STR)
app.include_router(comparison_router, prefix=settings.API_V1_STR)
app.include_router(progress_router, prefix=settings.API_V1_STR)

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "demo_mode": not bool(settings.GEMINI_API_KEY)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
