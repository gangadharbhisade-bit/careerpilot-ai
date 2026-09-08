import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_auth_and_profile():
    # Register user
    email = "test_user_counselor@careerpilot.ai"
    reg_res = client.post("/api/auth/register", json={
        "email": email,
        "password": "Password123!",
        "full_name": "Test Traveler"
    })
    if reg_res.status_code in [400, 409]:
        # User already exists, login
        reg_res = client.post("/api/auth/login", json={
            "email": email,
            "password": "Password123!"
        })
    assert reg_res.status_code == 200
    token = reg_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Fetch me
    me_res = client.get("/api/auth/me", headers=headers)
    assert me_res.status_code == 200
    assert me_res.json()["email"] == email

    # Profile get & update
    prof_res = client.get("/api/profile", headers=headers)
    assert prof_res.status_code == 200

    upd_res = client.put("/api/profile", json={
        "target_career": "AI Engineer",
        "skills": ["Python", "SQL", "Git"]
    }, headers=headers)
    assert upd_res.status_code == 200
    assert upd_res.json()["target_career"] == "AI Engineer"

def test_chat_api():
    guest_res = client.post("/api/auth/guest")
    token = guest_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    chat_res = client.post("/api/chat", json={
        "message": "I know basic Python, how can I become an AI Engineer?"
    }, headers=headers)
    assert chat_res.status_code == 200
    data = chat_res.json()
    assert "reply" in data
    assert "session_id" in data
    assert data["is_demo_mode"] in [True, False]

def test_roadmap_generation():
    rm_res = client.post("/api/roadmap/generate", json={
        "target_career": "AI Engineer",
        "duration": "6-month",
        "level": "Beginner"
    })
    assert rm_res.status_code == 200
    data = rm_res.json()
    assert data["target_career"] == "AI Engineer"
    assert len(data["phases"]) > 0

def test_skill_gap_analysis():
    sg_res = client.post("/api/skill-gap/analyze", json={
        "current_skills": ["Python", "SQL"],
        "target_role": "AI Engineer"
    })
    assert sg_res.status_code == 200
    data = sg_res.json()
    assert data["readiness_percentage"] >= 0.0
    assert "missing_skills" in data

def test_resume_analyzer():
    res_res = client.post("/api/resume/analyze", json={
        "target_role": "Software Developer",
        "resume_text": "Experienced Python developer skilled in React, FastAPI, SQL and Docker."
    })
    assert res_res.status_code == 200
    data = res_res.json()
    assert data["ats_score"] > 0
    assert "suggested_bullet_points" in data

def test_mock_interview():
    guest_res = client.post("/api/auth/guest")
    token = guest_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    start_res = client.post("/api/interview/start", json={
        "target_role": "Software Developer",
        "interview_type": "Technical"
    }, headers=headers)
    assert start_res.status_code == 200
    sess_id = start_res.json()["session_id"]

    ans_res = client.post("/api/interview/answer", json={
        "session_id": sess_id,
        "user_answer": "Asynchronous programming allows non-blocking execution of I/O operations."
    }, headers=headers)
    assert ans_res.status_code == 200
    assert ans_res.json()["previous_evaluation"]["score"] >= 1.0
