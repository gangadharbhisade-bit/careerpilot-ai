from typing import Dict, Any, List
from app.services.intent_router import classify_intent, detect_target_role, detect_topic, extract_comparison_roles, IntentType
from app.services.roadmap_engine import generate_roadmap

CAREER_DETAILS = {
    "Data Analyst": {
        "focus": "Business intelligence, data cleaning, KPI dashboards, and data-driven decision making",
        "key_skills": ["SQL", "Advanced Excel", "Power BI / Tableau", "Python (Pandas/NumPy)", "Statistics"],
        "coding_level": "Moderate (SQL Queries & Analytical Scripts)",
        "math_level": "Basic to Intermediate Descriptive Statistics",
        "learning_curve": "2 - 3 Months (Fast Entry Path)",
        "typical_projects": ["Executive Sales KPI Dashboard", "Customer Churn Analytics", "Financial Performance Report"]
    },
    "Data Scientist": {
        "focus": "Statistical modeling, predictive machine learning algorithms, and exploratory data science",
        "key_skills": ["Python", "Advanced SQL", "Statistics & Probability", "Scikit-Learn", "Machine Learning", "Seaborn"],
        "coding_level": "High (Data Engineering & ML Pipelines)",
        "math_level": "Advanced Linear Algebra, Calculus & Statistics",
        "learning_curve": "4 - 6 Months",
        "typical_projects": ["Predictive Customer Churn Model", "E-Commerce Recommendation System", "Price Prediction Pipeline"]
    },
    "AI Engineer": {
        "focus": "Building production AI applications, Large Language Models (LLMs), RAG architectures, and AI Agents",
        "key_skills": ["Python 3.11+", "PyTorch / TensorFlow", "LangChain & LlamaIndex", "Vector DBs (Chroma/Pinecone)", "FastAPI", "MLOps"],
        "coding_level": "Very High (Production AI Systems)",
        "math_level": "High (Neural Network Mathematics & Embeddings)",
        "learning_curve": "6 - 8 Months",
        "typical_projects": ["Document Q&A RAG Chatbot", "Autonomous AI Research Agent", "Deployed LLM Serving API"]
    },
    "Android Developer": {
        "focus": "Native mobile application development for Android OS ecosystem",
        "key_skills": ["Kotlin 2.0+", "Android Studio", "Jetpack Compose", "Room DB", "Retrofit REST APIs", "MVVM & Hilt"],
        "coding_level": "Very High (Native Mobile Architecture)",
        "math_level": "Basic Logical & Algorithmic Math",
        "learning_curve": "4 - 6 Months",
        "typical_projects": ["Full MVVM News & Weather App", "Task Manager with Jetpack Compose", "Play Store E-Commerce App"]
    },
    "iOS Developer": {
        "focus": "Native iOS, iPadOS and macOS application development for Apple ecosystem",
        "key_skills": ["Swift 5+", "Xcode IDE", "SwiftUI", "CoreData / SwiftData", "URLSession", "MVVM Architecture"],
        "coding_level": "Very High (Native Apple Frameworks)",
        "math_level": "Basic Logical & Algorithmic Math",
        "learning_curve": "4 - 6 Months",
        "typical_projects": ["SwiftUI Expense Tracker", "iOS Fitness App with CoreData", "App Store Published Product"]
    },
    "Frontend Developer": {
        "focus": "User interface development, web accessibility, and responsive client-side web applications",
        "key_skills": ["HTML5 & CSS3", "Tailwind CSS", "JavaScript ES6+", "TypeScript", "React 18", "Vite"],
        "coding_level": "High (Client-Side Logic & Component Design)",
        "math_level": "Basic Layout Geometry & Logic",
        "learning_curve": "3 - 5 Months",
        "typical_projects": ["Glassmorphic SaaS Landing Page", "TypeScript E-Commerce Storefront", "Personal Interactive Portfolio"]
    },
    "Backend Developer": {
        "focus": "Server-side business logic, REST/GraphQL APIs, database modeling, authentication, and cloud infrastructure",
        "key_skills": ["Python / Node.js / Go", "FastAPI / Express", "PostgreSQL / SQL", "Docker", "Redis", "JWT Auth"],
        "coding_level": "Very High (Distributed Systems & Database Operations)",
        "math_level": "Moderate Algorithmic & Relational Logic",
        "learning_curve": "4 - 6 Months",
        "typical_projects": ["Scalable E-Commerce REST API", "Real-Time Chat Engine", "Dockerized Microservice Suite"]
    },
    "Cybersecurity Engineer": {
        "focus": "Network defense, vulnerability assessments, security auditing, SIEM log analysis, and ethical hacking",
        "key_skills": ["TCP/IP & Networking", "Linux Administration", "Python/Bash Security Scripts", "OWASP Top 10", "Wireshark", "Splunk"],
        "coding_level": "Moderate (Automation & Exploit Analysis Scripts)",
        "math_level": "Cryptography & Mathematical Proofs",
        "learning_curve": "5 - 7 Months",
        "typical_projects": ["Custom Python Network Scanner", "Splunk Threat Hunting Dashboard", "Web Security Audit Report"]
    }
}

DEFAULT_CAREER_DETAIL = {
    "focus": "Building high-performance software systems, applications, and technology solutions",
    "key_skills": ["Core Programming", "Data Structures & Algorithms", "Version Control (Git)", "Database Systems"],
    "coding_level": "High",
    "math_level": "Moderate",
    "learning_curve": "4 - 6 Months",
    "typical_projects": ["Full-Stack Web/Mobile Application", "REST API Backend", "Portfolio Showcase"]
}

def generate_counselor_response(
    user_query: str,
    user_profile: Dict[str, Any] = None,
    history: List[Dict[str, Any]] = None
) -> Dict[str, Any]:
    intent = classify_intent(user_query, history, user_profile)
    target_role = detect_target_role(user_query, history, user_profile) or "Software Developer"
    topic = detect_topic(user_query)

    reply_markdown = ""
    structured_payload = {"intent": intent, "target_role": target_role}

    # 1. FREE RESOURCES / LEARNING RESOURCES INTENT
    if intent in [IntentType.FREE_RESOURCES, IntentType.LEARNING_RESOURCES]:
        req_topic = topic or (target_role if target_role != "Software Developer" else "Python")
        
        if req_topic.lower() == "python":
            reply_markdown = """🐍 **Python Complete Free Learning Path & Verified Resources**

Here is your dedicated 100% free learning path to master **Python**:

📍 **Phase 1: Python Core Foundations**
* Variables, Data Types (`int`, `str`, `float`, `bool`)
* Conditionals (`if / elif / else`) & Loops (`for`, `while`)
* Functions, Scope & Parameters
* Basic String Manipulation & Formatting

📍 **Phase 2: Data Structures & OOP**
* Lists, Dictionaries, Sets, Tuples
* Object-Oriented Programming (`class`, `__init__`, inheritance, methods)
* Exception Handling (`try / except`) & File I/O (`open()`, `with`)
* Standard Modules (`math`, `os`, `sys`, `json`)

📍 **Phase 3: Hands-On Practice & Projects**
* Build a CLI Expense Tracker or Weather Parser
* Solve 15 beginner coding challenges on HackerRank / LeetCode

🟢 **Verified 100% Free Learning Resources**:
1. 📖 [Official Python Documentation & Tutorial](https://docs.python.org/3/tutorial/) — *Official reference guide*
2. 💻 [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) — *Interactive free course*
3. 📘 [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — *Practical hands-on automation book*
4. 📊 [Kaggle Python Micro-Course](https://www.kaggle.com/learn/python) — *Data science & ML focused Python guide*

💡 **Counselor Advice**: Spend 1 hour daily writing code in VS Code or Jupyter Notebook. Practice matters 10x more than watching videos!"""

            structured_payload["resources"] = {
                "free": [
                    {"title": "Official Python Tutorial", "url": "https://docs.python.org/3/tutorial/"},
                    {"title": "freeCodeCamp Python Course", "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/"},
                    {"title": "Automate the Boring Stuff", "url": "https://automatetheboringstuff.com/"},
                    {"title": "Kaggle Python Micro-Course", "url": "https://www.kaggle.com/learn/python"}
                ]
            }
        else:
            reply_markdown = f"""📚 **Top Recommended Free Learning Resources for {req_topic}**

Here are verified, top-quality learning resources for **{req_topic}**:

🟢 **100% FREE RESOURCES**:
* 📖 **Official Documentation**: Always start with the official reference guides (MDN, Android Developers, Python Docs, PyTorch Docs)
* 💻 **freeCodeCamp** (freecodecamp.org) — Interactive full courses & certifications
* 📊 **Kaggle Learn** (kaggle.com/learn) — Hands-on micro-courses for Data & ML
* 🎥 **3Blue1Brown** (YouTube) — Visual intuition for Mathematics & Computer Science

📜 **PAID / CERTIFICATIONS**:
* **Coursera** — University-backed specializations
* **Udemy** — Project-based developer bootcamps

💻 **PRACTICE PLATFORMS**:
* **LeetCode / HackerRank / PortSwigger** — Domain-specific challenge practice

✅ **Your Next Step**: Pick ONE primary platform and complete 1 module per day!"""

            structured_payload["resources"] = {
                "free": [
                    {"title": f"Official {req_topic} Documentation", "url": "https://developer.mozilla.org/"},
                    {"title": "freeCodeCamp Courses", "url": "https://www.freecodecamp.org/"},
                    {"title": "Kaggle Learn", "url": "https://www.kaggle.com/learn"}
                ]
            }

    # 2. CAREER COMPARISON INTENT
    elif intent == IntentType.CAREER_COMPARISON:
        role_a, role_b = extract_comparison_roles(user_query)
        detail_a = CAREER_DETAILS.get(role_a, DEFAULT_CAREER_DETAIL)
        detail_b = CAREER_DETAILS.get(role_b, DEFAULT_CAREER_DETAIL)

        recommendation = f"Choose **{role_a}** if you prefer {detail_a['focus'].lower()}. Choose **{role_b}** if you prefer {detail_b['focus'].lower()}."

        reply_markdown = f"""📊 **Career Comparison: {role_a} vs {role_b}**

Here is a side-by-side technical comparison between **{role_a}** and **{role_b}**:

### 1. **{role_a}**
* **Primary Focus**: {detail_a['focus']}
* **Key Skills**: {', '.join(detail_a['key_skills'])}
* **Coding Depth**: {detail_a['coding_level']}
* **Math Level**: {detail_a['math_level']}
* **Learning Curve**: {detail_a['learning_curve']}

---

### 2. **{role_b}**
* **Primary Focus**: {detail_b['focus']}
* **Key Skills**: {', '.join(detail_b['key_skills'])}
* **Coding Depth**: {detail_b['coding_level']}
* **Math Level**: {detail_b['math_level']}
* **Learning Curve**: {detail_b['learning_curve']}

---

💡 **Counselor Verdict**: {recommendation}"""

        structured_payload["comparison_data"] = {
            "title": f"{role_a} vs {role_b}",
            "career_a": {
                "name": role_a,
                "focus": detail_a["focus"],
                "key_skills": detail_a["key_skills"],
                "coding_level": detail_a["coding_level"],
                "math_level": detail_a["math_level"],
                "learning_curve": detail_a["learning_curve"],
                "typical_projects": detail_a["typical_projects"]
            },
            "career_b": {
                "name": role_b,
                "focus": detail_b["focus"],
                "key_skills": detail_b["key_skills"],
                "coding_level": detail_b["coding_level"],
                "math_level": detail_b["math_level"],
                "learning_curve": detail_b["learning_curve"],
                "typical_projects": detail_b["typical_projects"]
            },
            "recommendation": recommendation
        }

    # 3. ROADMAP INTENT
    elif intent == IntentType.ROADMAP:
        roadmap_data = generate_roadmap(target_role, "6-month", "Beginner")
        
        phase_lines = []
        for phase in roadmap_data["phases"]:
            skills_str = ", ".join(phase["skills_covered"][:4])
            phase_lines.append(f"* **Phase {phase['phase_number']} ({phase['phase_title']})**: Focus on {skills_str}. *Milestone*: {phase['milestone_project']}")
            
        phases_markdown = "\n".join(phase_lines)

        reply_markdown = f"""🗺️ **{target_role} Career Roadmap**

🎯 **Target Goal**: Become a job-ready **{target_role}**
⏱️ **Estimated Duration**: 6 Months (10 - 15 hrs / week)

📍 **Phase-by-Phase Progression**:
{phases_markdown}

📚 **Recommended Learning Resources**:
* 🟢 **FREE**: Official Documentation, freeCodeCamp, Kaggle
* 📜 **CERTIFICATIONS**: Industry Recognized Certificates

💻 **Career Milestone Project**:
* Build and deploy a production-grade portfolio application showcasing clean architecture and unit tests.

✅ **Your Next Actionable Step**:
Click the button below to view the full visual interactive roadmap or start with Phase 1 fundamentals today!"""

        structured_payload["target_career"] = target_role
        structured_payload["roadmap_data"] = roadmap_data
        structured_payload["roadmap_overview"] = [
            {"phase": f"Phase {p['phase_number']}", "topic": p["phase_title"]}
            for p in roadmap_data["phases"]
        ]

    # 4. SKILL ADVICE INTENT ("Python me next kya sikhu?")
    elif intent == IntentType.SKILL_ADVICE:
        req_topic = topic or target_role
        reply_markdown = f"""🧠 **Recommended Next Skill Progression for {req_topic}**

Based on your current knowledge of **{req_topic}**, here is the most practical next skill progression:

1. **Relational Databases & SQL** (PostgreSQL / MySQL) — *Essential for data & server management*
2. **Specialized Core Frameworks** (FastAPI / React / Android Compose / Pandas depending on your track)
3. **Git & GitHub Version Control** — *To showcase repositories to recruiters*
4. **REST API Design & Security** — *Connecting applications safely*
5. **Docker & Cloud Deployment** — *Production deployment*

💡 **Why this order?**
Mastering SQL and specialized frameworks lets you immediately build end-to-end applications and stand out in hiring shortlists.

✅ **Your Next Step**: Spend 2 weeks building hands-on database queries and API integrations!"""

        structured_payload["skills_to_learn"] = [
            "SQL & PostgreSQL", "Specialized Frameworks", "Git & GitHub", "REST APIs", "Docker"
        ]

    # 5. JOB SEARCH INTENT
    elif intent == IntentType.JOB_SEARCH:
        reply_markdown = f"""💼 **Job & Internship Application Strategy for {target_role}**

📍 **Best Verified Hiring Platforms**:
1. **LinkedIn Jobs**: Best for full-time roles, direct recruiter messages & company alerts
2. **Wellfound (AngelList Talent)**: Best for high-growth tech startups & remote roles
3. **Internshala**: Top platform for verified stipended internships (for freshers)
4. **Indeed & Naukri**: High-volume job listings across MNCs and IT services
5. **Official Company Career Pages**: Always cross-apply directly on corporate career portals

🚨 **SCAM WARNING SHIELD**:
* **NEVER pay money** for job offers, training fees, or laptop security deposits. Legitimate employers PAY YOU.
* Verify official company email domains (e.g., hr@company.com).

✅ **Your Next Step**: Tailor your resume specifically for {target_role} and submit 3-5 applications daily on LinkedIn & Wellfound!"""

        structured_payload["application_channels"] = [
            {"name": "LinkedIn Jobs", "url": "https://www.linkedin.com/jobs/"},
            {"name": "Wellfound", "url": "https://wellfound.com/"},
            {"name": "Internshala", "url": "https://internshala.com/"}
        ]

    # 6. PROJECTS INTENT
    elif intent == IntentType.PROJECTS:
        reply_markdown = f"""💻 **Recommended Portfolio Projects for {target_role}**

🟢 **BEGINNER**:
* **CLI Utility / Foundation Tool**: Solves a specific data or string task with clean documentation.

🔵 **INTERMEDIATE**:
* **REST API & Interactive Web/Mobile App**: Complete CRUD operations, authentication, and API integration.

🟣 **ADVANCED**:
* **Production SaaS / Multi-Module Application**: Clean Architecture, unit test coverage, offline caching, and cloud/store deployment.

✅ **Your Next Step**: Build 1 solid intermediate project, write a detailed README.md, and pin it on your GitHub profile!"""

        structured_payload["projects"] = [
            {"title": f"Foundational {target_role} Tool", "difficulty": "Beginner"},
            {"title": f"Interactive {target_role} Application", "difficulty": "Intermediate"},
            {"title": f"Enterprise Production {target_role} Suite", "difficulty": "Advanced"}
        ]

    # 7. RESUME GUIDANCE INTENT
    elif intent == IntentType.RESUME:
        reply_markdown = f"""📄 **ATS-Friendly Resume Checklist for {target_role}**

1. **Clean Single-Column Format**: Avoid complex graphics or multi-column layouts that confuse ATS scanners.
2. **Role Keyword Matching**: Include exact core keywords for **{target_role}** in your Skills and Experience sections.
3. **Action-Impact Bullet Points**:
   * ❌ *Weak*: "Worked on a project."
   * ✅ *Strong*: "Engineered a production-grade application for {target_role}, improving system performance by 30% for 1,000+ active users."
4. **Hyperlinked GitHub Repositories**: Include direct clickable links to source code and live demos.

✅ **Your Next Step**: Launch our **Resume Assistant** tool in the left sidebar to run an automated ATS keyword audit!"""

    # 8. INTERVIEW PREPARATION INTENT
    elif intent == IntentType.INTERVIEW_PREPARATION:
        reply_markdown = f"""🎤 **Interview Preparation Guide for {target_role}**

📍 **Key Interview Stages**:
1. **HR & Behavioral Round**: STAR framework (Situation, Task, Action, Result).
2. **Core Fundamentals & Frameworks**: Deep technical questions on language internals and architecture.
3. **Live Coding / Problem Solving**: Data structures, algorithm puzzles, or practical domain tasks.
4. **System Design / App Architecture**: Scalability, state management, API design, and trade-offs.

✅ **Your Next Step**: Use our **Mock Interview Prep** tool in the left sidebar to practice interactive turn-by-turn question answering!"""

    # 9. CASUAL / GENERAL CONVERSATION
    elif intent == IntentType.CASUAL_CONVERSATION:
        reply_markdown = """👋 **Hello! I am CareerPilot AI**, your dedicated career counselor.

How can I guide your career today? You can ask me about:
* **Roadmaps** for Android, Data Analyst, Cybersecurity, Frontend, AI Engineer, etc.
* **Free learning resources** ("Python free me kaise sikhe?")
* **Career comparisons** ("Data Analyst vs Data Scientist")
* **Skill advice & portfolio projects**
* **Resume tips & Mock interview practice**

What career path would you like to discuss?"""

    # 10. GENERAL CAREER GUIDANCE (DEFAULT)
    else:
        reply_markdown = f"""🎯 **Career Guidance for {target_role}**

Thank you for reaching out! Here is practical career guidance:

1. **Focus on Hands-On Building**: Spend 70% of your learning time writing code and building projects.
2. **Quality over Quantity**: 2 polished GitHub projects with documentation matter more than 10 incomplete repositories.
3. **Continuous Practice**: Maintain a daily study streak of 1-2 hours.

✅ **Next Actionable Step**: Ask for a specific roadmap, free learning resources, or project ideas for **{target_role}**!"""

    return {
        "reply": reply_markdown,
        "structured_payload": structured_payload,
        "is_demo_mode": True
    }
