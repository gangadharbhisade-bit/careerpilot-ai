import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_data_isolation():
    # 1. Register Account A (Android Developer)
    email_a = "account_a_android@careerpilot.ai"
    reg_a = client.post("/api/auth/register", json={
        "email": email_a,
        "password": "Password123!",
        "full_name": "Test Android Developer"
    })
    if reg_a.status_code in [400, 409]:
        reg_a = client.post("/api/auth/login", json={"email": email_a, "password": "Password123!"})
    assert reg_a.status_code == 200
    token_a = reg_a.json()["access_token"]
    headers_a = {"Authorization": f"Bearer {token_a}"}

    # 2. Register Account B (Data Analyst)
    email_b = "account_b_data@careerpilot.ai"
    reg_b = client.post("/api/auth/register", json={
        "email": email_b,
        "password": "Password123!",
        "full_name": "Test Data Analyst"
    })
    if reg_b.status_code in [400, 409]:
        reg_b = client.post("/api/auth/login", json={"email": email_b, "password": "Password123!"})
    assert reg_b.status_code == 200
    token_b = reg_b.json()["access_token"]
    headers_b = {"Authorization": f"Bearer {token_b}"}

    # 3. Update Account A profile -> Android Developer
    upd_a = client.put("/api/profile", json={
        "target_career": "Android Developer",
        "skills": ["Kotlin", "Java"],
        "experience_level": "Beginner"
    }, headers=headers_a)
    assert upd_a.status_code == 200
    assert upd_a.json()["target_career"] == "Android Developer"

    # 4. Update Account B profile -> Data Analyst
    upd_b = client.put("/api/profile", json={
        "target_career": "Data Analyst",
        "skills": ["Excel", "SQL"],
        "experience_level": "Intermediate"
    }, headers=headers_b)
    assert upd_b.status_code == 200
    assert upd_b.json()["target_career"] == "Data Analyst"

    # 5. Verify Account A profile isolation
    prof_a = client.get("/api/profile", headers=headers_a).json()
    assert prof_a["target_career"] == "Android Developer"
    assert "Kotlin" in prof_a["skills"]

    # 6. Verify Account B profile isolation
    prof_b = client.get("/api/profile", headers=headers_b).json()
    assert prof_b["target_career"] == "Data Analyst"
    assert "Excel" in prof_b["skills"]
    assert "Kotlin" not in prof_b["skills"]

    # 7. Verify Account A progress & pending skills isolation
    prog_a = client.get("/api/progress", headers=headers_a).json()
    pending_a = [s.lower() for s in prog_a["pending_skills"]]
    assert any("compose" in s or "retrofit" in s or "room" in s for s in pending_a)
    assert not any("power bi" in s or "pandas" in s for s in pending_a)

    # 8. Verify Account B progress & pending skills isolation
    prog_b = client.get("/api/progress", headers=headers_b).json()
    pending_b = [s.lower() for s in prog_b["pending_skills"]]
    assert any("power bi" in s or "pandas" in s or "tableau" in s for s in pending_b)
    assert not any("jetpack compose" in s or "retrofit" in s for s in pending_b)

    # 9. Test IDOR protection on Chat Session History
    chat_a = client.post("/api/chat", json={"message": "Android Coroutines help"}, headers=headers_a)
    assert chat_a.status_code == 200
    sess_id_a = chat_a.json()["session_id"]

    # Account B attempts to read Account A's chat session history
    idor_res = client.get(f"/api/chat/history?session_id={sess_id_a}", headers=headers_b)
    assert idor_res.status_code in [403, 404]

    # 10. Verify Task isolation
    task_a = client.post("/api/progress/task/create", json={
        "task_text": "Private Android Task for User A",
        "date_str": "2026-09-08"
    }, headers=headers_a).json()
    
    prog_b_after = client.get("/api/progress", headers=headers_b).json()
    b_tasks = [t["task_text"] for t in prog_b_after["daily_planner"]["tasks"]]
    assert "Private Android Task for User A" not in b_tasks
