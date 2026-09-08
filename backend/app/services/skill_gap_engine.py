from typing import List, Dict, Any

# Skill normalization dictionary
SKILL_ALIASES = {
    "js": "JavaScript",
    "javascript": "JavaScript",
    "java script": "JavaScript",
    "ts": "TypeScript",
    "typescript": "TypeScript",
    "react": "React",
    "reactjs": "React",
    "react.js": "React",
    "py": "Python",
    "python": "Python",
    "python3": "Python",
    "kotlin": "Kotlin",
    "kotlin android": "Kotlin",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",
    "html": "HTML5",
    "html5": "HTML5",
    "css": "CSS3",
    "css3": "CSS3",
    "tailwind": "Tailwind CSS",
    "tailwindcss": "Tailwind CSS",
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "aws": "AWS (Amazon Web Services)",
    "docker": "Docker",
    "git": "Git & GitHub",
    "github": "Git & GitHub",
    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes"
}

ROLE_REQUIREMENTS: Dict[str, List[Dict[str, Any]]] = {
    "Android Developer": [
        {"skill": "Kotlin Programming", "priority": "CRITICAL", "hours": 40, "resource": "Kotlin Official Documentation"},
        {"skill": "Android Studio & IDE", "priority": "HIGH", "hours": 20, "resource": "Google Android Studio Basics"},
        {"skill": "Jetpack Compose UI", "priority": "CRITICAL", "hours": 45, "resource": "Google Android Compose Pathway"},
        {"skill": "Android Architecture (MVVM)", "priority": "HIGH", "hours": 35, "resource": "Android Developer Guide"},
        {"skill": "REST APIs & Retrofit", "priority": "CRITICAL", "hours": 25, "resource": "Retrofit Documentation"},
        {"skill": "Room Database & Storage", "priority": "HIGH", "hours": 25, "resource": "Room DB Training"},
        {"skill": "Kotlin Coroutines & Flow", "priority": "CRITICAL", "hours": 30, "resource": "Kotlin Coroutines Docs"},
        {"skill": "Hilt Dependency Injection", "priority": "MEDIUM", "hours": 20, "resource": "Dagger Hilt Docs"}
    ],
    "Data Analyst": [
        {"skill": "Advanced Excel & Pivot Tables", "priority": "CRITICAL", "hours": 25, "resource": "Microsoft Excel Learning Hub"},
        {"skill": "SQL & Relational Databases", "priority": "CRITICAL", "hours": 40, "resource": "Mode Analytics SQL Tutorial"},
        {"skill": "Statistics & Probability", "priority": "CRITICAL", "hours": 35, "resource": "Khan Academy Statistics"},
        {"skill": "Python (Pandas & NumPy)", "priority": "HIGH", "hours": 40, "resource": "Kaggle Pandas Course"},
        {"skill": "Power BI / Tableau", "priority": "CRITICAL", "hours": 35, "resource": "Microsoft Power BI Guided Learning"},
        {"skill": "Data Visualization (Seaborn)", "priority": "HIGH", "hours": 20, "resource": "Kaggle Data Viz"},
        {"skill": "Business Storytelling & Metrics", "priority": "MEDIUM", "hours": 15, "resource": "Harvard Business School Analytics"}
    ],
    "Cybersecurity Engineer": [
        {"skill": "Computer Networking & TCP/IP", "priority": "CRITICAL", "hours": 45, "resource": "Cisco Networking Academy"},
        {"skill": "Linux Systems Administration", "priority": "CRITICAL", "hours": 40, "resource": "Linux Journey"},
        {"skill": "Python / Bash Security Scripting", "priority": "HIGH", "hours": 30, "resource": "Automate the Boring Stuff"},
        {"skill": "Web Security (OWASP Top 10)", "priority": "CRITICAL", "hours": 50, "resource": "PortSwigger Web Security Academy"},
        {"skill": "Network Traffic Analysis (Wireshark)", "priority": "HIGH", "hours": 25, "resource": "Wireshark User Guide"},
        {"skill": "SIEM & Log Analysis (Splunk)", "priority": "MEDIUM", "hours": 30, "resource": "Splunk Fundamentals"},
        {"skill": "Cryptography & PKI", "priority": "HIGH", "hours": 25, "resource": "Coursera Cryptography"}
    ],
    "Frontend Developer": [
        {"skill": "Semantic HTML5 & Accessibility", "priority": "CRITICAL", "hours": 20, "resource": "MDN Web Docs"},
        {"skill": "Modern CSS & Tailwind CSS", "priority": "CRITICAL", "hours": 30, "resource": "freeCodeCamp Responsive Web Design"},
        {"skill": "JavaScript ES6+", "priority": "CRITICAL", "hours": 50, "resource": "JavaScript.info"},
        {"skill": "TypeScript", "priority": "HIGH", "hours": 25, "resource": "TypeScript Handbook"},
        {"skill": "React 18 & Component Design", "priority": "CRITICAL", "hours": 45, "resource": "React Official Docs (react.dev)"},
        {"skill": "State Management (Redux/Context)", "priority": "HIGH", "hours": 25, "resource": "Redux Toolkit Docs"},
        {"skill": "Vite & Modern Web Tooling", "priority": "MEDIUM", "hours": 15, "resource": "Vite Guide"}
    ],
    "Backend Developer": [
        {"skill": "Python / Node.js / Go", "priority": "CRITICAL", "hours": 45, "resource": "Official Language Docs"},
        {"skill": "FastAPI / Express.js Framework", "priority": "CRITICAL", "hours": 35, "resource": "FastAPI Documentation"},
        {"skill": "SQL & PostgreSQL Database Design", "priority": "CRITICAL", "hours": 40, "resource": "PostgreSQL Tutorial"},
        {"skill": "REST & GraphQL API Design", "priority": "HIGH", "hours": 25, "resource": "RESTful API Guide"},
        {"skill": "Authentication (JWT & OAuth2)", "priority": "HIGH", "hours": 20, "resource": "OAuth.net Guides"},
        {"skill": "Docker & Containerization", "priority": "HIGH", "hours": 25, "resource": "Docker Official Docs"},
        {"skill": "Caching (Redis)", "priority": "MEDIUM", "hours": 15, "resource": "Redis Documentation"}
    ],
    "AI Engineer": [
        {"skill": "Python 3.11+", "priority": "CRITICAL", "hours": 30, "resource": "Python Docs"},
        {"skill": "Mathematics for AI (Linear Algebra)", "priority": "CRITICAL", "hours": 30, "resource": "3Blue1Brown Linear Algebra"},
        {"skill": "NumPy & Pandas", "priority": "HIGH", "hours": 20, "resource": "Kaggle Pandas Course"},
        {"skill": "Machine Learning (Scikit-Learn)", "priority": "HIGH", "hours": 40, "resource": "Scikit-Learn Docs"},
        {"skill": "Deep Learning (PyTorch)", "priority": "CRITICAL", "hours": 50, "resource": "PyTorch Deep Learning Book"},
        {"skill": "Hugging Face & LLM Fine-Tuning", "priority": "CRITICAL", "hours": 35, "resource": "Hugging Face Course"},
        {"skill": "RAG & Vector DBs (Chroma/Pinecone)", "priority": "CRITICAL", "hours": 30, "resource": "LangChain Official Docs"},
        {"skill": "FastAPI & MLOps Serving", "priority": "MEDIUM", "hours": 25, "resource": "FastAPI Docs"}
    ],
    "Data Scientist": [
        {"skill": "Python 3", "priority": "CRITICAL", "hours": 30, "resource": "Python Docs"},
        {"skill": "Advanced SQL Queries", "priority": "CRITICAL", "hours": 35, "resource": "Mode Analytics SQL"},
        {"skill": "Statistics & Probability", "priority": "CRITICAL", "hours": 40, "resource": "Khan Academy Statistics"},
        {"skill": "Data Wrangling with Pandas", "priority": "CRITICAL", "hours": 30, "resource": "Pandas Docs"},
        {"skill": "Exploratory Data Analysis (Seaborn)", "priority": "HIGH", "hours": 20, "resource": "Kaggle Data Viz"},
        {"skill": "Machine Learning Algorithms", "priority": "HIGH", "hours": 50, "resource": "Scikit-Learn Docs"},
        {"skill": "A/B Testing & Experimentation", "priority": "HIGH", "hours": 25, "resource": "Udacity A/B Testing"}
    ],
    "Cloud / DevOps Engineer": [
        {"skill": "Linux Systems & CLI", "priority": "CRITICAL", "hours": 40, "resource": "Linux Journey"},
        {"skill": "Cloud Provider (AWS / GCP)", "priority": "CRITICAL", "hours": 50, "resource": "AWS Training & Certification"},
        {"skill": "Docker & Container Management", "priority": "CRITICAL", "hours": 30, "resource": "Docker Docs"},
        {"skill": "Kubernetes Orchestration", "priority": "CRITICAL", "hours": 45, "resource": "Kubernetes Basics"},
        {"skill": "Terraform Infrastructure as Code", "priority": "HIGH", "hours": 30, "resource": "HashiCorp Learn"},
        {"skill": "CI/CD Pipelines (GitHub Actions)", "priority": "HIGH", "hours": 25, "resource": "GitHub Actions Docs"}
    ]
}

def normalize_skill(skill_name: str) -> str:
    """Normalizes skill strings to standard names."""
    clean = skill_name.strip().lower()
    return SKILL_ALIASES.get(clean, skill_name.strip().title())

def get_required_skills_for_role(target_role: str) -> List[str]:
    """Returns standard required skill names for any target role."""
    reqs = ROLE_REQUIREMENTS.get(target_role)
    if not reqs:
        # Alias lookup
        for key, list_reqs in ROLE_REQUIREMENTS.items():
            if key.lower() in target_role.lower() or target_role.lower() in key.lower():
                reqs = list_reqs
                break
    if not reqs:
        reqs = ROLE_REQUIREMENTS["Backend Developer"]
    return [r["skill"] for r in reqs]

def analyze_skill_gap(current_skills: List[str], target_role: str) -> Dict[str, Any]:
    requirements = ROLE_REQUIREMENTS.get(target_role)
    if not requirements:
        for key, list_reqs in ROLE_REQUIREMENTS.items():
            if key.lower() in target_role.lower() or target_role.lower() in key.lower():
                requirements = list_reqs
                break
    if not requirements:
        requirements = ROLE_REQUIREMENTS["Backend Developer"]

    # Normalize user's current skills
    normalized_user = [normalize_skill(s).lower() for s in current_skills]
    
    required_skill_names = [req["skill"] for req in requirements]
    missing_skills_info = []
    matched_skills = []

    for req in requirements:
        req_name = req["skill"]
        req_clean = req_name.lower()
        
        # Exact or substring check against normalized current skills
        is_matched = False
        for user_sk in normalized_user:
            if user_sk in req_clean or req_clean in user_sk:
                is_matched = True
                break

        if is_matched:
            matched_skills.append(req_name)
        else:
            missing_skills_info.append(req)

    total_req_count = len(requirements)
    matched_count = len(matched_skills)
    readiness = round((matched_count / total_req_count) * 100, 1) if total_req_count > 0 else 0.0

    return {
        "target_role": target_role,
        "current_skills": current_skills,
        "required_skills": required_skill_names,
        "missing_skills": [m["skill"] for m in missing_skills_info],
        "readiness_percentage": readiness,
        "priority_order": missing_skills_info
    }
