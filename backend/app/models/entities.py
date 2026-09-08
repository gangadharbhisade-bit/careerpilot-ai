from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, JSON, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    chat_sessions = relationship("ChatSession", back_populates="user", cascade="all, delete-orphan")
    roadmaps = relationship("SavedRoadmap", back_populates="user", cascade="all, delete-orphan")
    interviews = relationship("InterviewSession", back_populates="user", cascade="all, delete-orphan")
    daily_tasks = relationship("DailyTask", back_populates="user", cascade="all, delete-orphan")


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)

    education = Column(String, nullable=True, default=None)
    degree = Column(String, nullable=True, default=None)
    branch = Column(String, nullable=True, default=None)
    current_role = Column(String, nullable=True, default=None)
    experience_level = Column(String, nullable=True, default="Beginner") # Beginner, Intermediate, Advanced
    skills = Column(JSON, nullable=True, default=list) # List of skills
    programming_languages = Column(JSON, nullable=True, default=list)
    interests = Column(JSON, nullable=True, default=list)
    target_career = Column(String, nullable=True, default=None)
    target_industry = Column(String, nullable=True, default="Technology")
    preferred_location = Column(String, nullable=True, default="Remote")
    remote_preference = Column(String, nullable=True, default="Remote") # Remote, On-site, Hybrid
    salary_expectation = Column(String, nullable=True, default=None)
    available_learning_time = Column(String, nullable=True, default="2 hours/day")
    career_goal = Column(Text, nullable=True, default=None)
    current_projects = Column(JSON, nullable=True, default=list)
    certifications = Column(JSON, nullable=True, default=list)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="profile")


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, default="Career Guidance Session")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="chat_sessions")
    messages = relationship("ChatMessage", back_populates="session", cascade="all, delete-orphan")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"), nullable=False)
    sender = Column(String, nullable=False) # "user" or "assistant"
    content = Column(Text, nullable=False)
    structured_payload = Column(JSON, nullable=True) # JSON payload for rendering roadmaps/cards
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    session = relationship("ChatSession", back_populates="messages")


class SavedRoadmap(Base):
    __tablename__ = "saved_roadmaps"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_role = Column(String, nullable=False)
    duration = Column(String, nullable=False) # e.g. "6-month", "3-month"
    level = Column(String, nullable=False) # "Beginner", "Intermediate", "Advanced"
    phases_json = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="roadmaps")


class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_role = Column(String, nullable=False)
    interview_type = Column(String, nullable=False) # HR, Technical, Coding, Behavioral, System Design
    status = Column(String, default="in_progress") # in_progress, completed
    questions_history = Column(JSON, default=list) # [{question, user_answer, score, feedback, suggested_answer}]
    overall_score = Column(Float, nullable=True)
    overall_feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="interviews")


class DailyTask(Base):
    __tablename__ = "daily_tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_text = Column(String, nullable=False)
    topic = Column(String, nullable=True)
    estimated_minutes = Column(Integer, default=30)
    completed = Column(Boolean, default=False)
    date_str = Column(String, nullable=False) # "YYYY-MM-DD"
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="daily_tasks")
