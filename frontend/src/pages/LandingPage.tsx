import React from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, Map, Compass, Video, BookOpen, ShieldCheck, ArrowRight, CheckCircle2 } from 'lucide-react';

export const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-[#0a0d14] text-slate-100 selection:bg-indigo-500 selection:text-white">
      {/* Navbar */}
      <header className="border-b border-white/10 bg-[#0a0d14]/80 backdrop-blur-md sticky top-0 z-50 px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center shadow-lg shadow-indigo-500/30">
            <Sparkles className="w-6 h-6 text-white" />
          </div>
          <span className="font-extrabold text-xl text-white tracking-wide">
            Career<span className="text-indigo-400">Pilot</span> <span className="text-xs bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30">AI</span>
          </span>
        </div>

        <div className="flex items-center space-x-4">
          <Link to="/login" className="text-xs text-slate-300 hover:text-white font-semibold">
            Sign In
          </Link>
          <Link
            to="/app/chat"
            className="gradient-btn px-5 py-2.5 rounded-xl text-xs font-bold text-white shadow-lg flex items-center space-x-2"
          >
            <span>Launch Counselor</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative pt-20 pb-16 px-6 text-center max-w-5xl mx-auto space-y-8">
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-indigo-600/20 rounded-full blur-[120px] pointer-events-none" />

        <div className="inline-flex items-center space-x-2 bg-indigo-500/10 border border-indigo-500/30 px-4 py-1.5 rounded-full text-xs text-indigo-300 font-semibold">
          <Sparkles className="w-4 h-4 text-indigo-400" />
          <span>AI-Powered Career Counselor Platform</span>
        </div>

        <h1 className="text-4xl sm:text-6xl font-extrabold text-white leading-tight tracking-tight">
          Build Your Career. <br />
          <span className="gradient-text">One Smart Step at a Time.</span>
        </h1>

        <p className="text-slate-400 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">
          AI-powered career guidance, personalized roadmaps, learning resources, skill gap analysis, target company insights, job portal guidance, and interview preparation — all in one platform.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
          <Link
            to="/app/roadmaps"
            className="gradient-btn px-8 py-4 rounded-2xl text-sm font-bold text-white shadow-xl shadow-indigo-600/30 flex items-center space-x-2 w-full sm:w-auto justify-center"
          >
            <span>Start Your Career Roadmap</span>
            <ArrowRight className="w-4 h-4" />
          </Link>

          <Link
            to="/app/chat"
            className="glass-panel hover:bg-white/10 px-8 py-4 rounded-2xl text-sm font-bold text-white border border-white/15 transition w-full sm:w-auto text-center"
          >
            Ask CareerPilot AI
          </Link>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-16 px-6 max-w-6xl mx-auto space-y-12">
        <div className="text-center space-y-2">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white">Everything You Need for Career Success</h2>
          <p className="text-slate-400 text-sm">Designed specifically for students, freshers, and tech professionals.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-indigo-600/20 flex items-center justify-center text-indigo-400 border border-indigo-500/30">
              <Map className="w-6 h-6" />
            </div>
            <h3 className="font-bold text-white text-lg">Roadmap Generator</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Generate 30-day, 3-month, 6-month, or 1-year structured roadmaps with weekly topics, practice tasks, and milestone projects.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-purple-600/20 flex items-center justify-center text-purple-400 border border-purple-500/30">
              <Compass className="w-6 h-6" />
            </div>
            <h3 className="font-bold text-white text-lg">Skill Gap Analyzer</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Upload your current skills and compute your readiness score against top market job requirements.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-cyan-600/20 flex items-center justify-center text-cyan-400 border border-cyan-500/30">
              <Video className="w-6 h-6" />
            </div>
            <h3 className="font-bold text-white text-lg">Mock Interview Prep</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Step-by-step AI interview simulation for HR, Technical, and System Design questions with real-time scoring.
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 py-8 px-6 text-center text-xs text-slate-500">
        <p>© 2026 CareerPilot AI – Intelligent Career Guidance & Roadmap Assistant. All rights reserved.</p>
      </footer>
    </div>
  );
};
