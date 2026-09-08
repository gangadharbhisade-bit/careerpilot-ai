# CareerPilot AI – Intelligent Career Guidance & Roadmap Assistant

**CareerPilot AI** is a production-ready, modern, secure, and highly reliable AI-powered career counseling web application. It helps students, freshers, and tech professionals make data-driven career decisions through personalized roadmaps, visual skill gap analysis, interactive turn-by-turn AI mock interviews, ATS resume auditing, curated verified learning resources, target company insights, and job portal guidance with scam alert protection.

---

## Key Features

1. **Structured AI Career Counselor Chatbot**:
   - Understands natural language questions in English and Hinglish (e.g. *"Mujhe Python aata hai, ab kya karu?"*, *"How to become an AI Engineer?"*).
   - Follows a strict 10-point counselor framework (Goal, Level, Skills, Roadmap, Resources, Projects, Job Channels, Interview Prep, Next Steps).
   - Includes prompt injection protection and system prompt shielding.

2. **Dedicated Career Roadmap Generator Engine**:
   - Dynamic 30-day, 3-month, 6-month, and 1-year roadmaps across 30+ career tracks.
   - Interactive weekly breakdown, practice tasks, milestone projects, and direct links.

3. **Skill Gap Analyzer**:
   - Visual readiness gauge matching user skill inventory against market role requirements.
   - Priority learning order with estimated hours and recommended resources.

4. **Interactive AI Mock Interview System**:
   - HR, Technical, Coding, and System Design interview simulations.
   - Real-time turn-by-turn evaluation (scoring 1–10, strengths, weaknesses, sample improved answers) and final summary card.

5. **Resume Assistant & ATS Auditor**:
   - ATS compatibility score calculator, core keyword matching, and impact-driven bullet point improver.

6. **Verified Learning Resources & Target Companies**:
   - Curated official documentation, interactive practice platforms, and top video courses with FREE/PAID/CERTIFICATION badges.
   - Direct official career portals for top hiring companies (Google, Microsoft, AWS, TCS, Startups).

7. **Job Portal Guidance & Scam Alert Shield**:
   - Verified platforms (LinkedIn, Wellfound, Indeed, Internshala) and anti-scam security warnings.

8. **Career Comparison Matrix & Daily Planner**:
   - Side-by-side career comparison matrix (e.g., Data Scientist vs. AI Engineer).
   - Daily learning task checklist and progress tracking.

9. **Intelligent Fallback / Demo Mode**:
   - Operates 100% out-of-the-box without requiring an external AI API key.
   - Automatically switches to live Google Gemini / OpenAI generation when API keys are configured in `.env`.

---

## Tech Stack

- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, Lucide Icons, Framer Motion, Recharts, React Markdown.
- **Backend**: Python FastAPI, SQLAlchemy ORM, Pydantic v2, Direct Bcrypt password hashing, PyJWT, Rate Limiting Middleware.
- **Database**: SQLite (default local zero-setup) / PostgreSQL compatible.
- **Testing**: `pytest` backend suite.
- **Deployment**: Vercel Serverless Functions, Docker, Docker Compose, Nginx.

---

## ☁️ Vercel Deployment

CareerPilot AI is ready for instant deployment to **Vercel**!

### Quick Deployment Instructions:
1. Import your GitHub repository into Vercel.
2. Add Environment Variables:
   - `VITE_API_URL`: Your backend URL (if split) or leave empty if deploying mono-project.
   - `SECRET_KEY`: Custom JWT secret hash.
   - `GEMINI_API_KEY`: Your Gemini API key.
   - `DATABASE_URL`: PostgreSQL connection string (Supabase / Neon) for production persistence.
3. Deploy!

For complete step-by-step instructions, see [docs/VERCEL_DEPLOYMENT.md](file:///C:/Users/LENOVO/.gemini/antigravity/scratch/careerpilot-ai/docs/VERCEL_DEPLOYMENT.md).

---

## Project Structure

```
careerpilot-ai/
├── frontend/
│   ├── src/
│   │   ├── components/      # Glassmorphic UI components (Sidebar, Header, ChatWindow, Modals)
│   │   ├── pages/           # LandingPage, ChatPage, RoadmapPage, SkillGapPage, ResumePage, InterviewPage, JobsPage, CompanyPage, ComparePage, PlannerPage, DashboardPage, ProfilePage
│   │   ├── services/        # api.ts
│   │   ├── context/         # AuthContext.tsx, ProfileContext.tsx
│   │   ├── types/           # index.ts
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── backend/
│   ├── app/
│   │   ├── api/             # FastAPI Endpoint Routers (auth, profile, chat, roadmap, skill_gap, resources, jobs, companies, resume, interview, comparison, progress)
│   │   ├── core/            # Config, Database, Security, Rate Limiter, Logger
│   │   ├── models/          # SQLAlchemy Database Entities
│   │   ├── schemas/         # Pydantic Validation Schemas
│   │   ├── services/        # AI Service, Fallback Counselor Engine, Roadmap Engine, Skill Gap Engine, Resume Engine, Interview Engine
│   │   └── main.py          # FastAPI App Entrypoint
│   ├── tests/               # Pytest Suite (test_backend.py)
│   └── requirements.txt
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Quick Start / Local Setup

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python app/main.py
```
Backend runs at: `http://127.0.0.1:8000` (Swagger Docs at `http://127.0.0.1:8000/docs`).

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at: `http://localhost:3000`.

### 3. Run Backend Test Suite
```bash
cd backend
python -m pytest tests/test_backend.py
```

---

## Docker Setup

Run the entire full-stack application via Docker Compose:

```bash
docker-compose up --build
```
Access the application at `http://localhost:3000`.

---

## License & Security Notes

- Passwords are pre-hashed with SHA256 before bcrypt digest calculation to guarantee 100% security and zero buffer overflow issues.
- Rate limiting middleware (120 req/min) protects all API endpoints against brute force and DDoS attacks.
- Input sanitization strips out prompt injection patterns.
