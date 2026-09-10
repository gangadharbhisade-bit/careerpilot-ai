# 🚀 CareerPilot AI — Next-Gen AI Career Guidance Platform

CareerPilot AI is an advanced, production-grade career guidance platform powered by **FastAPI**, **React 18 (Vite + TypeScript)**, and **Google Gemini AI**. It provides personalized career roadmaps, intelligent chatbot counseling, skill gap analysis, resume enhancement, mock interviews, target company insights, and daily learning roadmaps with 100% strict user data isolation.

---

## ✨ Features

- 🔐 **Strict Multi-User Isolation**: User-specific profiles, chat sessions, saved roadmaps, interview records, and daily tasks.
- 🎯 **Dynamic Career Roadmap Engine**: Role-aware curriculum generator supporting Android Developer, Data Analyst, AI Engineer, Frontend Developer, Cybersecurity Engineer, and dynamic fallbacks for custom target roles.
- 🤖 **Dynamic Intent Chatbot**: Intent routing engine distinguishing career roadmap requests, free learning resource inquiries, role comparison queries (e.g. Data Analyst vs Data Scientist), and general counseling.
- 📊 **Skill Gap Analyzer**: Real-time gap analysis comparing user's current skills against target role requirements with match score calculations.
- 📝 **Resume Assistant**: Automated ATS keyword optimization and bullet point enhancer.
- 🎤 **AI Mock Interview Simulator**: Question generator and real-time answer scoring with actionable feedback.
- 🏢 **Target Companies & Job Market Insights**: Detailed hiring requirements, interview tips, and salary ranges.
- 📅 **Daily Study Planner**: Automated task generation based on active career goals.

---

## 🏗️ Project Architecture

```
careerpilot-ai/
├── api/
│   └── index.py                # Serverless entrypoint for Vercel backend
├── backend/
│   ├── app/
│   │   ├── api/                # FastAPI Routers (auth, profile, chat, roadmap, skill_gap, etc.)
│   │   ├── core/               # App config, database session, security, rate limiter
│   │   ├── models/             # SQLAlchemy ORM models
│   │   ├── schemas/            # Pydantic validation schemas
│   │   ├── services/           # Intent router, roadmap engine, AI service, skill gap engine, etc.
│   │   └── main.py             # FastAPI App instance & middleware configuration
│   ├── tests/                  # Pytest test suite (100% passing)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/         # Modular React components & chat window
│   │   ├── context/            # AuthContext & ProfileContext
│   │   ├── pages/              # 12 React views (Dashboard, Roadmap, SkillGap, Chat, etc.)
│   │   └── services/           # API fetch client handling production base URLs
│   ├── package.json
│   └── vite.config.ts
├── docs/
│   ├── VERCEL_DEPLOYMENT.md    # Step-by-step Vercel Deployment Guide
│   └── RENDER_DEPLOYMENT.md    # Step-by-step Render Deployment Guide
├── .env.example                # Sample environment variables
├── render.yaml                 # Render Blueprint for 1-click deployment
└── vercel.json                 # Vercel monorepo rewrite configuration
```

---

## 🛠️ Local Development Setup

### 1. Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app/main.py
```
Backend will run at `http://localhost:8000`.

### 2. Frontend Setup (React + Vite)
```bash
cd frontend
npm install
npm run dev
```
Frontend will run at `http://localhost:5173`.

---

## 🧪 Running Automated Tests

Run the backend test suite:
```bash
# From repository root:
$env:PYTHONPATH="backend"; python -m pytest backend/tests
```
*(All 33 backend tests cover auth isolation, intent routing, dynamic metrics, and roadmap engine)*.

---

## ☁️ Production Deployment

### 1. Deploying to Vercel
Detailed guide: [`docs/VERCEL_DEPLOYMENT.md`](./docs/VERCEL_DEPLOYMENT.md)

- Deploy directly using `vercel.json` and `api/index.py`.
- Configure `DATABASE_URL` (PostgreSQL via Neon / Supabase), `SECRET_KEY`, and `GEMINI_API_KEY` in Vercel settings.

### 2. Deploying to Render
Detailed guide: [`docs/RENDER_DEPLOYMENT.md`](./docs/RENDER_DEPLOYMENT.md)

- Use the 1-click `render.yaml` Blueprint file in Render Dashboard.
- Automatically provisions Managed PostgreSQL Database, FastAPI Web Service, and React Static Site.

---

## 📄 License
MIT License. Built for CareerPilot AI.
