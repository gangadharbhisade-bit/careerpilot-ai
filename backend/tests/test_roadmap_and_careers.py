import pytest
from app.services.roadmap_engine import generate_roadmap
from app.services.intent_router import classify_intent, detect_target_role, IntentType
from app.services.fallback_engine import generate_counselor_response

# TEST 1: Android Developer roadmap
def test_android_developer_roadmap():
    data = generate_roadmap("Android Developer", "6-month", "Beginner")
    assert data["target_career"] == "Android Developer"
    phase_titles = [p["phase_title"] for p in data["phases"]]
    assert any("Kotlin" in t or "Android" in t for t in phase_titles)
    # Must NOT contain AI Engineer content
    all_skills = [s for p in data["phases"] for s in p["skills_covered"]]
    assert "PyTorch" not in all_skills
    assert "Kotlin 2.0+" in all_skills or "Jetpack Compose" in all_skills

# TEST 2: Data Analyst roadmap
def test_data_analyst_roadmap():
    data = generate_roadmap("Data Analyst", "6-month", "Beginner")
    assert data["target_career"] == "Data Analyst"
    all_skills = [s for p in data["phases"] for s in p["skills_covered"]]
    assert "Advanced Excel" in all_skills or "SQL Queries" in all_skills
    assert "Power BI / Tableau" in all_skills

# TEST 3: Cybersecurity Engineer roadmap
def test_cybersecurity_roadmap():
    data = generate_roadmap("Cybersecurity Engineer", "6-month", "Beginner")
    assert data["target_career"] == "Cybersecurity Engineer"
    all_skills = [s for p in data["phases"] for s in p["skills_covered"]]
    assert "OWASP Top 10" in all_skills or "TCP/IP Stack" in all_skills

# TEST 4: Frontend Developer roadmap
def test_frontend_roadmap():
    data = generate_roadmap("Frontend Developer", "6-month", "Beginner")
    assert data["target_career"] == "Frontend Developer"
    all_skills = [s for p in data["phases"] for s in p["skills_covered"]]
    assert "React 18" in all_skills or "TypeScript" in all_skills

# TEST 5: AI Engineer roadmap
def test_ai_engineer_roadmap():
    data = generate_roadmap("AI Engineer", "6-month", "Beginner")
    assert data["target_career"] == "AI Engineer"
    all_skills = [s for p in data["phases"] for s in p["skills_covered"]]
    assert "PyTorch" in all_skills or "Scikit-Learn" in all_skills

# TEST 6: Profile Goal = AI Engineer, User Query = Android Developer -> Android wins!
def test_explicit_query_overrides_profile_goal():
    profile = {"target_career": "AI Engineer", "education": "B.Tech"}
    msg = "Android Developer kaise bane?"
    role = detect_target_role(msg, profile=profile)
    assert role == "Android Developer"
    res = generate_counselor_response(msg, user_profile=profile)
    assert "Android Developer" in res["reply"]
    assert "Kotlin" in res["reply"] or "Android" in res["reply"]
    assert "AI Engineer" not in res["reply"]

# TEST 7: "Python aata hai, ab kya seekhu?" -> SKILL_ADVICE
def test_python_next_skill_guidance():
    msg = "Python aata hai, ab kya seekhu?"
    intent = classify_intent(msg)
    assert intent == IntentType.SKILL_ADVICE
    res = generate_counselor_response(msg)
    assert "Skill Progression" in res["reply"]
    assert "Month 1 (Foundations)" not in res["reply"]

# TEST 8: "Android Developer ke liye projects batao" -> Android projects
def test_android_projects_guidance():
    msg = "Android Developer ke liye projects batao"
    intent = classify_intent(msg)
    role = detect_target_role(msg)
    assert intent == IntentType.PROJECTS
    assert role == "Android Developer"
    res = generate_counselor_response(msg)
    assert "Android" in res["reply"]

# TEST 9: "Data Analyst vs Data Scientist" -> Comparison
def test_data_analyst_vs_scientist_comparison():
    msg = "Data Analyst vs Data Scientist"
    intent = classify_intent(msg)
    assert intent == IntentType.CAREER_COMPARISON
    res = generate_counselor_response(msg)
    assert "Matrix" in res["reply"] or "Comparison" in res["reply"]

# TEST 10: "Resume kaise banau?" -> Resume guidance
def test_resume_guidance_intent():
    msg = "Resume kaise banau?"
    intent = classify_intent(msg)
    assert intent == IntentType.RESUME
    res = generate_counselor_response(msg)
    assert "ATS" in res["reply"] or "Resume" in res["reply"]
