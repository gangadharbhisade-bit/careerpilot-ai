# Vercel Deployment Guide — CareerPilot AI

This guide walks you through deploying **CareerPilot AI** (React + Vite Frontend & FastAPI Backend) to [Vercel](https://vercel.com).

---

## 🏗️ Architecture Overview

* **Frontend**: React 18 + TypeScript + Vite (Static Web App).
* **Backend**: FastAPI Serverless Function via Vercel Python Runtime (`api/index.py`).
* **Database**:
  * **Development / Local**: SQLite (`sqlite:///./careerpilot.db`).
  * **Vercel Serverless Production**: PostgreSQL (Supabase / Neon / ElephantSQL) via `DATABASE_URL` for persistent multi-user data storage. If `DATABASE_URL` is omitted, serverless fallback uses `/tmp/careerpilot.db`.

---

## 🚀 Option 1: One-Click Single Project Deployment on Vercel

If you deploy your GitHub repository directly to Vercel as a single project:

1. Push your project to GitHub:
   ```bash
   git add .
   git commit -m "Deploy CareerPilot AI to Vercel"
   git push origin main
   ```
2. Go to [Vercel Dashboard](https://vercel.com/dashboard) and click **Add New** → **Project**.
3. Import your `careerpilot-ai` GitHub repository.
4. Set the **Framework Preset** to **Other** (or Vite).
5. In **Environment Variables**, add:
   * `SECRET_KEY`: `your_custom_jwt_secret_hash`
   * `ENVIRONMENT`: `production`
   * `GEMINI_API_KEY`: `your_gemini_api_key`
   * `DATABASE_URL`: `postgresql://user:password@ep-host.neon.tech/neondb` *(Recommended PostgreSQL URL from Neon.tech or Supabase)*
   * `ALLOWED_ORIGINS`: `https://your-project.vercel.app`
6. Click **Deploy**.
   Vercel will compile the Vite frontend static files and route `/api/*` requests directly to `api/index.py` serverless function!

---

## 🚀 Option 2: Split Frontend & Backend Deployment (Recommended for High Scale)

If you prefer to host Frontend and Backend as separate Vercel projects:

### Step 1: Deploy Backend (`/backend`)
1. Create a Vercel project pointing to your repo.
2. Set **Root Directory** to `backend` (or root if using `api/index.py`).
3. Add Environment Variables:
   * `SECRET_KEY`: `your_secret`
   * `ENVIRONMENT`: `production`
   * `GEMINI_API_KEY`: `your_gemini_key`
   * `ALLOWED_ORIGINS`: `https://careerpilot-frontend.vercel.app`
   * `DATABASE_URL`: `postgresql://...`
4. Deploy to get your backend URL: `https://careerpilot-backend.vercel.app`.

### Step 2: Deploy Frontend (`/frontend`)
1. Create another Vercel project pointing to your repo.
2. Set **Root Directory** to `frontend`.
3. Framework Preset: **Vite**.
4. Add Environment Variable:
   * `VITE_API_URL`: `https://careerpilot-backend.vercel.app`
5. Deploy to get your frontend URL: `https://careerpilot-frontend.vercel.app`.

---

## 📊 Database Persistence Note (SQLite vs PostgreSQL)

* **Local Dev**: SQLite runs out-of-the-box (`./careerpilot.db`).
* **Vercel Serverless Production**: Vercel serverless containers are ephemeral and have a read-only filesystem (except `/tmp`).
* For **permanent production user data persistence**, obtain a free PostgreSQL database URL from **Neon.tech** or **Supabase** and set the `DATABASE_URL` environment variable in Vercel.

---

## ✅ Deployment Verification Checklist

- [x] `api/index.py` Vercel entrypoint configured.
- [x] `vercel.json` routing configured.
- [x] CORS regex matching enabled for `*.vercel.app`.
- [x] `VITE_API_URL` environment variable support in `frontend/src/services/api.ts`.
- [x] Localhost development (`npm run dev` & `python app/main.py`) remains 100% operational.
