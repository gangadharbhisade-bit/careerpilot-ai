import React, { useState, useEffect } from 'react';
import { LayoutDashboard, Compass, Map, Video, FileText, CheckCircle2, TrendingUp, Sparkles, Target, Award, ArrowRight } from 'lucide-react';
import { apiService } from '../services/api';
import { useProfile } from '../context/ProfileContext';
import { useAuth } from '../context/AuthContext';
import { Link } from 'react-router-dom';

const ONBOARDING_CAREERS = [
  'Android Developer',
  'Data Analyst',
  'Cybersecurity Engineer',
  'Frontend Developer',
  'Backend Developer',
  'AI Engineer',
  'Data Scientist',
  'Cloud / DevOps Engineer',
  'Full Stack Developer',
  'iOS Developer'
];

export const DashboardPage: React.FC = () => {
  const { user } = useAuth();
  const { profile, updateProfile, refetchProfile } = useProfile();
  const [progress, setProgress] = useState<any>(null);
  const [loadingProgress, setLoadingProgress] = useState(true);

  // Onboarding modal/card state
  const [selectedCareer, setSelectedCareer] = useState(profile.target_career || '');
  const [customCareer, setCustomCareer] = useState('');
  const [selectedLevel, setSelectedLevel] = useState(profile.experience_level || 'Beginner');
  const [savingOnboarding, setSavingOnboarding] = useState(false);

  const fetchDashboardData = async () => {
    setLoadingProgress(true);
    try {
      const data = await apiService.getProgress();
      setProgress(data);
    } catch (err) {
      console.error('Error fetching progress:', err);
    } finally {
      setLoadingProgress(false);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, [profile.target_career, user?.id]);

  const handleSaveCareer = async () => {
    const finalCareer = customCareer.trim() || selectedCareer;
    if (!finalCareer) return;

    setSavingOnboarding(true);
    try {
      await updateProfile({
        target_career: finalCareer,
        experience_level: selectedLevel,
        career_goal: `Become a professional ${finalCareer}`
      });
      await fetchDashboardData();
    } catch (err) {
      console.error(err);
    } finally {
      setSavingOnboarding(false);
    }
  };

  const hasTargetCareer = Boolean(profile.target_career);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      {/* Top Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 relative overflow-hidden">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-2 text-indigo-400 text-xs font-bold uppercase mb-1">
              <Sparkles className="w-4 h-4" />
              <span>Career Execution Center</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white">
              Welcome Back, {user?.full_name || 'Career Navigator'}!
            </h1>
            <p className="text-slate-400 text-sm mt-1">
              Target Goal: <strong className="text-indigo-300">{profile.target_career || 'Not Set (Set Below)'}</strong> • Level: {profile.experience_level || 'Beginner'}
            </p>
          </div>

          <Link
            to="/app/chat"
            className="gradient-btn px-5 py-3 rounded-2xl text-xs font-bold text-white flex items-center space-x-2 shrink-0"
          >
            <Sparkles className="w-4 h-4" />
            <span>Consult AI Counselor</span>
          </Link>
        </div>
      </div>

      {/* Onboarding Banner if Target Career not set */}
      {!hasTargetCareer && (
        <div className="glass-panel p-6 rounded-3xl border-2 border-indigo-500/50 bg-indigo-950/20 space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-3 bg-indigo-600/30 rounded-2xl text-indigo-400 border border-indigo-500/40">
              <Target className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">Set Your Target Career Goal</h2>
              <p className="text-xs text-slate-300 mt-0.5">
                Choose your career path to unlock your role-aware roadmap, dynamic skill matrix, and tailored counselor guidance.
              </p>
            </div>
          </div>

          <div className="space-y-3 pt-2">
            <label className="text-xs font-semibold text-slate-300">Select Career Role:</label>
            <div className="flex flex-wrap gap-2">
              {ONBOARDING_CAREERS.map((c) => (
                <button
                  key={c}
                  type="button"
                  onClick={() => { setSelectedCareer(c); setCustomCareer(''); }}
                  className={`text-xs px-3.5 py-2 rounded-xl border transition ${
                    selectedCareer === c && !customCareer
                      ? 'bg-indigo-600 text-white border-indigo-400 font-bold shadow-lg shadow-indigo-500/30'
                      : 'bg-white/5 hover:bg-white/10 text-slate-300 border-white/10'
                  }`}
                >
                  {c}
                </button>
              ))}
            </div>

            <div className="flex items-center space-x-2 pt-1">
              <span className="text-xs text-slate-400">Or type custom role:</span>
              <input
                type="text"
                value={customCareer}
                onChange={(e) => { setCustomCareer(e.target.value); setSelectedCareer(''); }}
                placeholder="e.g. Game Developer, Full Stack..."
                className="bg-white/5 border border-white/10 rounded-xl px-3 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
              />
            </div>

            <div className="pt-2 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center space-x-2">
                <span className="text-xs text-slate-300 font-semibold">Experience Level:</span>
                {['Beginner', 'Intermediate', 'Advanced'].map((lvl) => (
                  <button
                    key={lvl}
                    type="button"
                    onClick={() => setSelectedLevel(lvl)}
                    className={`text-xs px-3 py-1 rounded-lg border transition ${
                      selectedLevel === lvl
                        ? 'bg-purple-600 text-white border-purple-400 font-bold'
                        : 'bg-white/5 text-slate-400 border-white/10'
                    }`}
                  >
                    {lvl}
                  </button>
                ))}
              </div>

              <button
                type="button"
                onClick={handleSaveCareer}
                disabled={savingOnboarding || (!selectedCareer && !customCareer)}
                className="gradient-btn px-6 py-2.5 rounded-xl text-xs font-bold text-white flex items-center space-x-2 disabled:opacity-50"
              >
                <span>{savingOnboarding ? 'Personalizing...' : 'Save & Personalize Dashboard'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Analytics KPI Row */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="glass-panel p-5 rounded-2xl border border-white/10 space-y-2">
          <div className="flex items-center justify-between text-indigo-400">
            <TrendingUp className="w-5 h-5" />
            <span className="text-[10px] bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded-full font-bold">Overall</span>
          </div>
          <p className="text-xs text-slate-400">Career Readiness Score</p>
          <h2 className="text-2xl font-extrabold text-white">
            {progress?.overall_readiness_score !== undefined ? `${progress.overall_readiness_score}%` : '0%'}
          </h2>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-white/10 space-y-2">
          <div className="flex items-center justify-between text-purple-400">
            <Video className="w-5 h-5" />
            <span className="text-[10px] bg-purple-500/20 text-purple-300 px-2 py-0.5 rounded-full font-bold">Mock AI</span>
          </div>
          <p className="text-xs text-slate-400">Interview Readiness</p>
          <h2 className="text-2xl font-extrabold text-white">
            {progress?.interview_readiness_score !== undefined ? `${progress.interview_readiness_score}%` : '0%'}
          </h2>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-white/10 space-y-2">
          <div className="flex items-center justify-between text-cyan-400">
            <FileText className="w-5 h-5" />
            <span className="text-[10px] bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded-full font-bold">ATS Audit</span>
          </div>
          <p className="text-xs text-slate-400">Resume Alignment</p>
          <h2 className="text-2xl font-extrabold text-white">
            {progress?.resume_readiness_score !== undefined ? `${progress.resume_readiness_score}%` : '0%'}
          </h2>
        </div>

        <div className="glass-panel p-5 rounded-2xl border border-white/10 space-y-2">
          <div className="flex items-center justify-between text-emerald-400">
            <CheckCircle2 className="w-5 h-5" />
            <span className="text-[10px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded-full font-bold">Daily</span>
          </div>
          <p className="text-xs text-slate-400">Task Completion Rate</p>
          <h2 className="text-2xl font-extrabold text-white">
            {progress?.daily_planner?.completion_percentage !== undefined ? `${progress.daily_planner.completion_percentage}%` : '0%'}
          </h2>
        </div>
      </div>

      {/* Main Grid: Skills Inventory & Quick Tools */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column: Completed & Pending Skills */}
        <div className="lg:col-span-2 glass-panel p-6 rounded-3xl border border-white/10 space-y-6">
          <h3 className="text-sm font-bold text-white uppercase tracking-wider">Skills Progress Matrix</h3>

          <div className="space-y-4">
            <div>
              <h4 className="text-xs font-semibold text-emerald-400 mb-2">Mastered Skills</h4>
              {progress?.completed_skills && progress.completed_skills.length > 0 ? (
                <div className="flex flex-wrap gap-2">
                  {progress.completed_skills.map((s: string, idx: number) => (
                    <span key={idx} className="bg-emerald-500/10 text-emerald-300 border border-emerald-500/30 text-xs px-3 py-1 rounded-full">
                      ✓ {s}
                    </span>
                  ))}
                </div>
              ) : (
                <p className="text-xs text-slate-500 italic">No skills added yet. Update your profile or complete roadmap phases.</p>
              )}
            </div>

            <div>
              <h4 className="text-xs font-semibold text-amber-400 mb-2">Pending Roadmap Milestones</h4>
              {progress?.pending_skills && progress.pending_skills.length > 0 ? (
                <div className="flex flex-wrap gap-2">
                  {progress.pending_skills.map((s: string, idx: number) => (
                    <span key={idx} className="bg-amber-500/10 text-amber-300 border border-amber-500/30 text-xs px-3 py-1 rounded-full">
                      ⏱ {s}
                    </span>
                  ))}
                </div>
              ) : (
                <p className="text-xs text-slate-500 italic">
                  {hasTargetCareer ? 'All core roadmap milestones completed!' : 'Select a target career above to generate pending milestones.'}
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Right Column: Quick Action Launchpad */}
        <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
          <h3 className="text-sm font-bold text-white uppercase tracking-wider">Quick Launchpad</h3>

          <div className="space-y-2">
            <Link
              to="/app/roadmaps"
              className="flex items-center justify-between p-3.5 rounded-xl bg-white/5 hover:bg-white/10 text-xs font-semibold text-white transition border border-white/10"
            >
              <div className="flex items-center space-x-2">
                <Map className="w-4 h-4 text-indigo-400" />
                <span>View Career Roadmap</span>
              </div>
              <span>→</span>
            </Link>

            <Link
              to="/app/skill-gap"
              className="flex items-center justify-between p-3.5 rounded-xl bg-white/5 hover:bg-white/10 text-xs font-semibold text-white transition border border-white/10"
            >
              <div className="flex items-center space-x-2">
                <Compass className="w-4 h-4 text-purple-400" />
                <span>Analyze Skill Gap</span>
              </div>
              <span>→</span>
            </Link>

            <Link
              to="/app/interview"
              className="flex items-center justify-between p-3.5 rounded-xl bg-white/5 hover:bg-white/10 text-xs font-semibold text-white transition border border-white/10"
            >
              <div className="flex items-center space-x-2">
                <Video className="w-4 h-4 text-cyan-400" />
                <span>Practice Mock Interview</span>
              </div>
              <span>→</span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};
