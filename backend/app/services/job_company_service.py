"""
Verified job platforms, target company databases, and scam safety warnings.
"""

LEGITIMATE_JOB_PLATFORMS = [
    {
        "name": "LinkedIn Jobs",
        "url": "https://www.linkedin.com/jobs/",
        "category": "Global / Professional",
        "free_badge": True,
        "description": "Top network for full-time, remote, and internship roles. Direct connection with recruiters."
    },
    {
        "name": "Indeed",
        "url": "https://www.indeed.com/",
        "category": "Global",
        "free_badge": True,
        "description": "Largest job search engine covering freshers, experienced, and specialized technical roles."
    },
    {
        "name": "Wellfound (formerly AngelList Talent)",
        "url": "https://wellfound.com/",
        "category": "Startups / Remote",
        "free_badge": True,
        "description": "Best portal for high-growth tech startups, early-stage AI startups, and equity-based hiring."
    },
    {
        "name": "Internshala",
        "url": "https://internshala.com/",
        "category": "Internships & Freshers",
        "free_badge": True,
        "description": "Popular platform for college students and freshers looking for verified stipended internships."
    },
    {
        "name": "Naukri.com",
        "url": "https://www.naukri.com/",
        "category": "India / Asia",
        "free_badge": True,
        "description": "Dominant hiring platform in India for tech, IT services, product companies, and MNCs."
    },
    {
        "name": "Glassdoor Jobs",
        "url": "https://www.glassdoor.com/Job/",
        "category": "Global / Company Reviews",
        "free_badge": True,
        "description": "Search job listings alongside real employee salary reports and interview questions."
    },
    {
        "name": "Y Combinator Work at a Startup",
        "url": "https://www.workatastartup.com/",
        "category": "Top YC Startups",
        "free_badge": True,
        "description": "Apply directly to Y-Combinator funded tech startups hiring software & AI engineers."
    }
]

SCAM_WARNING_RULES = [
    "🚨 NEVER pay money to get a job offer, interview slot, or training bond. Legitimate employers PAY YOU, not the other way around.",
    "🚨 Beware of unsolicited job offers sent via WhatsApp, Telegram, or unofficial Gmail/Yahoo addresses.",
    "🚨 Verify official domain emails (e.g. hr@company.com instead of company_careers_hr@gmail.com).",
    "🚨 Never share bank account passwords, OTPs, or sensitive financial information during interviews.",
    "🚨 Verify job openings directly on the official company careers portal before submitting applications."
]

TARGET_COMPANIES = {
    "AI Engineer": [
        {"name": "Google / DeepMind", "careers_url": "https://careers.google.com/", "type": "Big Tech", "focus": "LLMs, Computer Vision, Gemini"},
        {"name": "Microsoft", "careers_url": "https://careers.microsoft.com/", "type": "Big Tech", "focus": "Azure AI, OpenAI Partner, Copilot"},
        {"name": "Amazon / AWS", "careers_url": "https://www.amazon.jobs/", "type": "Big Tech", "focus": "Bedrock, AWS ML, Recommendation Systems"},
        {"name": "NVIDIA", "careers_url": "https://www.nvidia.com/en-us/about-nvidia/careers/", "type": "Hardware / AI Platform", "focus": "CUDA, TensorRT, Autonomous AI"},
        {"name": "OpenAI", "careers_url": "https://openai.com/careers/", "type": "AI Lab", "focus": "GPT Models, Frontier Research, Alignment"},
        {"name": "TCS AI Labs", "careers_url": "https://www.tcs.com/careers", "type": "IT Services Giant", "focus": "Enterprise AI Solutions"}
    ],
    "Software Developer": [
        {"name": "Microsoft", "careers_url": "https://careers.microsoft.com/", "type": "Product", "focus": "Cloud, Distributed Systems, Windows"},
        {"name": "Atlassian", "careers_url": "https://www.atlassian.com/company/careers", "type": "Product / SaaS", "focus": "Jira, Confluence, Cloud Architecture"},
        {"name": "Adobe", "careers_url": "https://www.adobe.com/careers.html", "type": "Product / Creative", "focus": "Creative Cloud, Document Cloud"},
        {"name": "Infosys", "careers_url": "https://www.infosys.com/careers/", "type": "Global IT Services", "focus": "Full Stack, Java, Cloud"},
        {"name": "Uber", "careers_url": "https://www.uber.com/us/en/careers/", "type": "High Scale Mobility", "focus": "Microservices, Real-time Systems"}
    ],
    "Data Scientist": [
        {"name": "Meta (Facebook)", "careers_url": "https://www.metacareers.com/", "type": "Big Tech", "focus": "Ad Recommendation, User Behavioral Data"},
        {"name": "Netflix", "careers_url": "https://jobs.netflix.com/", "type": "Media Tech", "focus": "Personalization Engines, A/B Testing"},
        {"name": "Spotify", "careers_url": "https://www.lifeatspotify.com/", "type": "Music Streaming", "focus": "Audio Recommendation, Behavioral Analytics"},
        {"name": "Fractal Analytics", "careers_url": "https://fractal.ai/careers/", "type": "Analytics Specialist", "focus": "Enterprise AI & Decision Sciences"}
    ],
    "Cybersecurity Engineer": [
        {"name": "Palo Alto Networks", "careers_url": "https://www.paloaltonetworks.com/company/careers", "type": "Security Enterprise", "focus": "Cloud Security, Next-Gen Firewalls"},
        {"name": "CrowdStrike", "careers_url": "https://www.crowdstrike.com/careers/", "type": "Endpoint Security", "focus": "Threat Intelligence, Falcon Platform"},
        {"name": "Cloudflare", "careers_url": "https://www.cloudflare.com/careers/", "type": "Edge & DDoS Security", "focus": "Zero Trust, Edge Compute Security"}
    ],
    "Cloud/DevOps Engineer": [
        {"name": "AWS", "careers_url": "https://aws.amazon.com/careers/", "type": "Cloud Provider", "focus": "Infrastructure, IAM, Kubernetes"},
        {"name": "Datadog", "careers_url": "https://www.datadoghq.com/careers/", "type": "Observability", "focus": "Monitoring, Distributed Tracing"},
        {"name": "HashiCorp", "careers_url": "https://www.hashicorp.com/careers", "type": "DevOps Infrastructure", "focus": "Terraform, Vault, Nomad"}
    ]
}

def get_job_platforms():
    return LEGITIMATE_JOB_PLATFORMS

def get_scam_warnings():
    return SCAM_WARNING_RULES

def get_target_companies(career: str):
    return TARGET_COMPANIES.get(career, TARGET_COMPANIES.get("Software Developer"))
