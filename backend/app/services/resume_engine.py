import re
from typing import Dict, Any, List

KEYWORD_DICTIONARIES = {
    "AI Engineer": ["python", "pytorch", "tensorflow", "scikit-learn", "numpy", "pandas", "llm", "rag", "transformers", "huggingface", "vector database", "fastapi", "docker", "mlops", "langchain", "prompt engineering"],
    "Software Developer": ["javascript", "typescript", "react", "node.js", "python", "fastapi", "sql", "postgresql", "rest api", "git", "docker", "data structures", "algorithms", "unit testing", "ci/cd"],
    "Data Scientist": ["python", "sql", "pandas", "numpy", "statistics", "machine learning", "tableau", "a/b testing", "data visualization", "seaborn", "scikit-learn", "data cleaning"],
}

def analyze_resume(resume_text: str, target_role: str) -> Dict[str, Any]:
    keywords = KEYWORD_DICTIONARIES.get(target_role, KEYWORD_DICTIONARIES["Software Developer"])
    text_lower = resume_text.lower()
    
    matched = [kw for kw in keywords if kw in text_lower]
    missing = [kw for kw in keywords if kw not in text_lower]
    
    score = int((len(matched) / len(keywords)) * 100) if keywords else 50
    # Keep score within reasonable bounds for feedback
    ats_score = min(max(score, 35), 95)
    
    strengths = []
    if len(matched) > 4:
        strengths.append(f"Strong keyword alignment for {target_role} ({', '.join(matched[:5])}).")
    if "project" in text_lower or "built" in text_lower or "developed" in text_lower:
        strengths.append("Contains action verbs indicating project experience.")
    if "education" in text_lower or "degree" in text_lower or "university" in text_lower:
        strengths.append("Clear educational background section.")
        
    improvements = []
    if missing:
        improvements.append(f"Add missing core keywords: {', '.join(missing[:5])}.")
    if not re.search(r'\b\d+%\b|\b\d+x\b|\b\d+ users\b', text_lower):
        improvements.append("Quantify achievements (e.g. 'Improved speed by 35%', 'Served 1,000+ users').")
    if ats_score < 70:
        improvements.append("Use a clean, single-column layout without complex graphics or tables for better ATS parsing.")

    suggested_bullet_points = [
        {
            "original": "Worked on a Python project for machine learning.",
            "improved": "Engineered a predictive Machine Learning pipeline using Python and Scikit-Learn, achieving 92% classification accuracy across 50,000 dataset records."
        },
        {
            "original": "Created a web app using React.",
            "improved": "Architected a responsive single-page web app with React, TypeScript, and Tailwind CSS, reducing page load latency by 40%."
        },
        {
            "original": "Assisted team with database queries.",
            "improved": "Optimized complex PostgreSQL queries and database indexing, reducing API response times by 30% for high-throughput endpoints."
        }
    ]

    actionable_next_steps = [
        f"Incorporate missing target keywords into your 'Skills' and 'Projects' sections: {', '.join(missing[:4])}.",
        "Rephrase project bullet points using the Action Verb + Context + Quantified Impact framework.",
        "Ensure resume filename is professional (e.g. Firstname_Lastname_Resume.pdf)."
    ]

    return {
        "ats_score": ats_score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "strengths": strengths if strengths else ["Basic structure identified."],
        "improvements": improvements,
        "suggested_bullet_points": suggested_bullet_points,
        "actionable_next_steps": actionable_next_steps
    }
