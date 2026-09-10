import re
from typing import Dict, Any, List, Optional, Tuple

class IntentType:
    ROADMAP = "ROADMAP"
    SKILL_ADVICE = "SKILL_ADVICE"
    LEARNING_RESOURCES = "LEARNING_RESOURCES"
    FREE_RESOURCES = "FREE_RESOURCES"
    JOB_SEARCH = "JOB_SEARCH"
    COMPANIES = "COMPANIES"
    RESUME = "RESUME"
    INTERVIEW_PREPARATION = "INTERVIEW_PREPARATION"
    CAREER_COMPARISON = "CAREER_COMPARISON"
    CAREER_SELECTION = "CAREER_SELECTION"
    PROJECTS = "PROJECTS"
    SALARY_INFORMATION = "SALARY_INFORMATION"
    CASUAL_CONVERSATION = "CASUAL_CONVERSATION"
    GENERAL_CAREER_GUIDANCE = "GENERAL_CAREER_GUIDANCE"

CAREER_ROLE_PATTERNS = {
    "Android Developer": [r"\bandroid developer\b", r"\bandroid dev\b", r"\bandroid app\b", r"\bkotlin developer\b", r"\bandroid\b"],
    "iOS Developer": [r"\bios developer\b", r"\bios dev\b", r"\bswift developer\b", r"\bios\b", r"\bswiftui\b"],
    "Flutter Developer": [r"\bflutter developer\b", r"\bflutter\b", r"\bdart developer\b"],
    "Data Analyst": [r"\bdata analyst\b", r"\bbusiness analyst\b", r"\bdata analytics\b", r"\bpowerbi\b", r"\btableau\b"],
    "Data Scientist": [r"\bdata scientist\b", r"\bdata science\b"],
    "Cybersecurity Engineer": [r"\bcyber\b", r"\bcybersecurity\b", r"\bethical hacking\b", r"\bsecurity analyst\b", r"\bpenetration tester\b", r"\bsoc analyst\b"],
    "Frontend Developer": [r"\bfrontend\b", r"\bfront-end\b", r"\breact developer\b", r"\bweb developer\b", r"\bangular\b", r"\bvue\b"],
    "Backend Developer": [r"\bbackend\b", r"\bback-end\b", r"\bnode developer\b", r"\bexpress\b", r"\bfastapi\b"],
    "Full Stack Developer": [r"\bfull stack\b", r"\bfullstack\b", r"\bmern\b", r"\bmean\b"],
    "AI Engineer": [r"\bai engineer\b", r"\bai/ml engineer\b", r"\bgenerative ai\b", r"\bllm engineer\b", r"\bai developer\b"],
    "Machine Learning Engineer": [r"\bmachine learning engineer\b", r"\bml engineer\b"],
    "Data Engineer": [r"\bdata engineer\b", r"\big data\b", r"\bspark developer\b"],
    "Cloud / DevOps Engineer": [r"\bcloud engineer\b", r"\bdevops\b", r"\baws engineer\b", r"\bsre\b", r"\bkubernetes\b", r"\bterraform\b"],
    "Java Developer": [r"\bjava developer\b", r"\bjava dev\b", r"\bspring boot\b"],
    "QA / Automation Engineer": [r"\bqa engineer\b", r"\bautomation tester\b", r"\bsoftware testing\b", r"\bqa\b", r"\bcypress\b", r"\bselenium\b"],
    "Game Developer": [r"\bgame developer\b", r"\bunity\b", r"\bunreal engine\b", r"\bgame dev\b"],
    "Blockchain Developer": [r"\bblockchain\b", r"\bsolidity\b", r"\bweb3\b", r"\bcrypto developer\b"],
    "UI/UX Designer": [r"\bui/ux\b", r"\bproduct designer\b", r"\bfigma\b", r"\bui designer\b"],
    "Software Developer": [r"\bsoftware developer\b", r"\bsoftware engineer\b", r"\bsde\b", r"\bprogrammer\b", r"\bdeveloper\b"]
}

TOPIC_PATTERNS = {
    "Python": [r"\bpython\b", r"\bpy\b"],
    "Java": [r"\bjava\b"],
    "JavaScript": [r"\bjavascript\b", r"\bjs\b"],
    "TypeScript": [r"\btypescript\b", r"\bts\b"],
    "React": [r"\breact\b", r"\breactjs\b"],
    "SQL": [r"\bsql\b", r"\bpostgres\b", r"\bmysql\b"],
    "Kotlin": [r"\bkotlin\b"],
    "Docker": [r"\bdocker\b", r"\bcontainers\b"],
    "Machine Learning": [r"\bmachine learning\b", r"\bml\b"],
    "Deep Learning": [r"\bdeep learning\b", r"\bpytorch\b", r"\btensorflow\b"]
}

def detect_topic(message: str) -> Optional[str]:
    msg_lower = message.lower()
    for topic, patterns in TOPIC_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, msg_lower):
                return topic
    return None

def detect_target_role(message: str, history: List[Dict[str, Any]] = None, profile: Dict[str, Any] = None) -> Optional[str]:
    msg_lower = message.lower()
    
    for role, patterns in CAREER_ROLE_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, msg_lower):
                return role

    if history:
        for prev_msg in reversed(history[-4:]):
            content = prev_msg.get("content", "").lower()
            for role, patterns in CAREER_ROLE_PATTERNS.items():
                for pat in patterns:
                    if re.search(pat, content):
                        return role

    if profile and profile.get("target_career"):
        return profile.get("target_career")

    return None

def extract_comparison_roles(message: str) -> Tuple[str, str]:
    msg_lower = message.lower()
    found_roles = []
    for role, patterns in CAREER_ROLE_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, msg_lower):
                if role not in found_roles:
                    found_roles.append(role)
                break
    if len(found_roles) >= 2:
        return found_roles[0], found_roles[1]
    elif len(found_roles) == 1:
        if found_roles[0] == "Data Analyst":
            return "Data Analyst", "Data Scientist"
        elif found_roles[0] == "Android Developer":
            return "Android Developer", "iOS Developer"
        else:
            return found_roles[0], "Software Developer"
    return "Data Analyst", "Data Scientist"

def classify_intent(message: str, history: List[Dict[str, Any]] = None, profile: Dict[str, Any] = None) -> str:
    msg_lower = message.lower()
    
    if any(k in msg_lower for k in [" vs ", "versus", "difference", "compare", "dono me kya farak", "farak kya", "farak hai"]):
        return IntentType.CAREER_COMPARISON

    if any(k in msg_lower for k in ["resume", "cv", "ats", "bullet point"]):
        return IntentType.RESUME

    if any(k in msg_lower for k in ["interview", "mock interview", "hr round", "technical round", "coding round"]):
        return IntentType.INTERVIEW_PREPARATION

    if any(k in msg_lower for k in ["free", "course", "courses", "resources", "tutorial", "books", "kaha se seekhu", "kaise sikhe", "kaise seekhu", "kaise seekho", "where to learn", "seekhne ke liye"]):
        if any(c in msg_lower for c in ["free", "free me", "batao", "resources", "course", "courses", "kaise sikhe", "kaha से"]):
            return IntentType.FREE_RESOURCES if "free" in msg_lower else IntentType.LEARNING_RESOURCES

    if any(k in msg_lower for k in ["google", "microsoft", "amazon", "company", "companies", "tcs", "infosys", "konse company"]):
        return IntentType.COMPANIES

    if any(k in msg_lower for k in ["job", "jobs", "internship", "internships", "apply", "kaha apply", "where to apply", "hiring", "fresher job"]):
        return IntentType.JOB_SEARCH

    if any(k in msg_lower for k in ["project", "projects", "portfolio", "kya banau", "what to build"]):
        return IntentType.PROJECTS

    if any(k in msg_lower for k in ["aata hai", "know python", "know sql", "ab kya", "after learning", "next step", "what to learn next", "ab mujhe kya", "next kya", "kya sikhu", "kya seekhu", "sikhu", "seekhu"]):
        return IntentType.SKILL_ADVICE

    if any(k in msg_lower for k in ["confused", "which career", "konse career", "kaunsi career", "suitable for me", "decide", "kya karu"]):
        return IntentType.CAREER_SELECTION

    if any(k in msg_lower for k in ["roadmap", "roadmap do", "kaise bane", "how to become", "steps to become", "6 month", "30 day", "path", "start karu", "kaise start"]):
        return IntentType.ROADMAP

    if any(k in msg_lower for k in ["salary", "pay", "ctc", "package", "earnings"]):
        return IntentType.SALARY_INFORMATION

    if any(k in msg_lower for k in ["hi", "hello", "hey", "thanks", "thank you", "kaise ho", "who are you"]):
        return IntentType.CASUAL_CONVERSATION

    return IntentType.GENERAL_CAREER_GUIDANCE
