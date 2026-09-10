# Render Deployment Guide — CareerPilot AI

This guide walks you through deploying **CareerPilot AI** (FastAPI Backend + React Static Site + PostgreSQL) to [Render](https://render.com).

---

## 🏗️ Architecture Overview on Render

* **Backend**: Web Service running Python / FastAPI with Uvicorn.
* **Frontend**: Static Site running Vite React build, with single-page app (SPA) rewrite rules.
* **Database**: Render Managed PostgreSQL Database (Free tier).

---

## 🚀 Deployment Option 1: 1-Click Render Blueprint (Recommended)

CareerPilot AI includes a `render.yaml` Blueprint file at the repository root.

### Steps:
1. Push your code to GitHub / GitLab:
   ```bash
   git add .
   git commit -m "Add Render blueprint configuration"
   git push origin main
   ```
2. Log into your [Render Dashboard](https://dashboard.render.com).
3. Click **New +** → **Blueprint**.
4. Connect your `careerpilot-ai` repository.
5. Render will automatically detect the `render.yaml` Blueprint file and create:
   - **PostgreSQL Database** (`careerpilot-db`)
   - **FastAPI Web Service** (`careerpilot-ai-backend`)
   - **React Static Site** (`careerpilot-ai-frontend`)
6. Enter your `GEMINI_API_KEY` (and optional `OPENAI_API_KEY`) in the environment prompt.
7. Click **Apply**. Render will automatically provision all services!

---

## 🛠️ Deployment Option 2: Manual Setup on Render

If you prefer to configure services manually:

### Step 1: Create a Managed PostgreSQL Database
1. Go to [Render Dashboard](https://dashboard.render.com) → **New +** → **PostgreSQL**.
2. Name: `careerpilot-db`.
3. Database: `careerpilot`, User: `careerpilot_user`.
4. Select **Free** plan.
5. Save the **Internal Database URL** (e.g. `postgres://careerpilot_user:pass@dpg-...-a/careerpilot`).

### Step 2: Deploy Backend Web Service
1. Click **New +** → **Web Service**.
2. Connect your repository.
3. Configuration:
   - **Name**: `careerpilot-ai-backend`
   - **Root Directory**: Leave blank (or `backend`)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Add Environment Variables:
   - `ENVIRONMENT`: `production`
   - `SECRET_KEY`: *(click Generate or enter a strong secret string)*
   - `DATABASE_URL`: *(paste your PostgreSQL Internal Database URL)*
   - `GEMINI_API_KEY`: *(your Gemini API key)*
   - `ALLOWED_ORIGINS`: `https://careerpilot-ai-frontend.onrender.com`
5. Click **Create Web Service**. Note your backend URL (e.g., `https://careerpilot-ai-backend.onrender.com`).

### Step 3: Deploy Frontend Static Site
1. Click **New +** → **Static Site**.
2. Connect your repository.
3. Configuration:
   - **Name**: `careerpilot-ai-frontend`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist` (or `./frontend/dist`)
4. Add Environment Variable:
   - `VITE_API_URL`: `https://careerpilot-ai-backend.onrender.com`
5. Under **Redirects / Rewrites**, add a rewrite rule:
   - **Source**: `/*`
   - **Destination**: `/index.html`
   - **Action**: `Rewrite`
6. Click **Create Static Site**.

---

## ✅ Deployment Verification Checklist

- [x] Backend connects to PostgreSQL database (`DATABASE_URL`).
- [x] CORS regex accepts `.onrender.com` domain.
- [x] React single-page routing works (`/* -> /index.html`).
- [x] All APIs (Auth, Roadmaps, Chatbot, Resume, Interview, Skill Gap) function smoothly in production environment.
