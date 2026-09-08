from fastapi import APIRouter
from app.schemas.schemas import CompareRequest, CompareResponse

router = APIRouter(prefix="/comparison", tags=["Career Comparison"])

COMPARISON_DATA = {
    "Data Scientist vs AI Engineer": {
        "career_a": "Data Scientist",
        "career_b": "AI Engineer",
        "summary": "Data Scientists analyze complex datasets to uncover business insights and build statistical models. AI Engineers build, deploy, and scale deep learning, LLM, and multi-agent AI systems into production software.",
        "comparison_table": [
            {"metric_name": "Core Focus", "career_a_value": "Statistics, EDA, Insights & Prediction", "career_b_value": "Neural Nets, LLMs, RAG & AI Agent Engineering"},
            {"metric_name": "Primary Language", "career_a_value": "Python, R, SQL", "career_b_value": "Python, C++, TypeScript"},
            {"metric_name": "Math Requirement", "career_a_value": "High (Statistics, Probability, A/B Testing)", "career_b_value": "High (Linear Algebra, Matrix Calculus)"},
            {"metric_name": "Primary Tools", "career_a_value": "Pandas, Scikit-Learn, SQL, Tableau", "career_b_value": "PyTorch, HuggingFace, LangChain, Vector DBs"},
            {"metric_name": "Deployment Focus", "career_a_value": "Medium (Notebooks, Dashboards)", "career_b_value": "Very High (FastAPI, Docker, MLOps, GPUs)"},
            {"metric_name": "Estimated Learning Time", "career_a_value": "4 - 6 Months", "career_b_value": "6 - 9 Months"},
            {"metric_name": "Salary Realities (Entry-Mid)", "career_a_value": "$85,000 - $130,000 / year", "career_b_value": "$100,000 - $160,000 / year"}
        ],
        "verdict_guidance": "If you enjoy statistical modeling and uncovering business stories from data, choose Data Scientist. If you love building autonomous AI applications, LLM agents, and high-performance software systems, choose AI Engineer!"
    },
    "Frontend Developer vs Full Stack Developer": {
        "career_a": "Frontend Developer",
        "career_b": "Full Stack Developer",
        "summary": "Frontend Developers specialize in crafting visually appealing, fast, and accessible user interfaces. Full Stack Developers build both frontend UIs and backend APIs/databases.",
        "comparison_table": [
            {"metric_name": "Core Focus", "career_a_value": "UI/UX Design Systems, Client State & Responsiveness", "career_b_value": "End-to-End System Architecture (UI + API + DB)"},
            {"metric_name": "Primary Stack", "career_a_value": "HTML, CSS, React, TypeScript, Tailwind", "career_b_value": "React, Node.js/FastAPI, PostgreSQL, Docker"},
            {"metric_name": "Estimated Learning Time", "career_a_value": "3 - 4 Months", "career_b_value": "6 - 8 Months"},
            {"metric_name": "Salary Realities (Entry-Mid)", "career_a_value": "$70,000 - $110,000 / year", "career_b_value": "$85,000 - $140,000 / year"}
        ],
        "verdict_guidance": "Start with Frontend if you love visual design and user interaction. Upgrade to Full Stack as you add database and API skills!"
    }
}

@router.post("/compare", response_model=CompareResponse)
def compare_careers(req: CompareRequest):
    key = f"{req.career_a} vs {req.career_b}"
    key_reverse = f"{req.career_b} vs {req.career_a}"

    if key in COMPARISON_DATA:
        return COMPARISON_DATA[key]
    elif key_reverse in COMPARISON_DATA:
        return COMPARISON_DATA[key_reverse]
        
    # Default dynamic fallback
    return {
        "career_a": req.career_a,
        "career_b": req.career_b,
        "summary": f"Comparison between {req.career_a} and {req.career_b}.",
        "comparison_table": [
            {"metric_name": "Role Focus", "career_a_value": f"Specialized in {req.career_a} workflows", "career_b_value": f"Specialized in {req.career_b} workflows"},
            {"metric_name": "Learning Curve", "career_a_value": "Moderate (3-6 Months)", "career_b_value": "Moderate to High (4-8 Months)"},
            {"metric_name": "Key Requirement", "career_a_value": "Domain expertise & problem solving", "career_b_value": "Technical proficiency & project experience"}
        ],
        "verdict_guidance": f"Both {req.career_a} and {req.career_b} offer excellent career growth. Choose based on your interest in daily technical tasks!"
    }
