import os
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

def get_database_url() -> str:
    db_url = os.getenv("DATABASE_URL", "")
    if db_url:
        # SQLAlchemy 1.4+ requires postgresql:// instead of legacy postgres://
        if db_url.startswith("postgres://"):
            return db_url.replace("postgres://", "postgresql://", 1)
        return db_url
    
    # Check if running in Vercel Serverless environment
    if "VERCEL" in os.environ:
        return "sqlite:////tmp/careerpilot.db"
    
    return "sqlite:///./careerpilot.db"

def get_allowed_origins() -> List[str]:
    origins = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    env_origins = os.getenv("ALLOWED_ORIGINS", "")
    if env_origins:
        for o in env_origins.split(","):
            if o.strip() and o.strip() not in origins:
                origins.append(o.strip())
                
    frontend_url = os.getenv("FRONTEND_URL", "")
    if frontend_url and frontend_url not in origins:
        origins.append(frontend_url.strip())
        
    vercel_url = os.getenv("VERCEL_URL", "")
    if vercel_url:
        formatted = f"https://{vercel_url}" if not vercel_url.startswith("http") else vercel_url
        if formatted not in origins:
            origins.append(formatted)
            
    return origins

class Settings(BaseSettings):
    PROJECT_NAME: str = "CareerPilot AI"
    API_V1_STR: str = "/api"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "careerpilot-ai-super-secret-jwt-key-2026-secure-hash")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    # Database
    DATABASE_URL: str = get_database_url()
    
    # AI Credentials
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Environment & CORS
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    ALLOWED_ORIGINS: List[str] = get_allowed_origins()

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
