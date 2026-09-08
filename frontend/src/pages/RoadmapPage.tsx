import React, { useState, useEffect } from 'react';
import { useSearchParams, useLocation } from 'react-router-dom';
import {
  Map,
  Clock,
  CheckCircle2,
  BookOpen,
  ExternalLink,
  Sparkles,
  Award,
  Layers,
  ChevronRight,
  Code,
  Briefcase,
  Zap,
  Target
} from 'lucide-react';
import { apiService } from '../services/api';
import { RoadmapData } from '../types';
import { useProfile } from '../context/ProfileContext';

const CAREER_OPTIONS = [
  'Android Developer',
  'Data Analyst',
  'Cybersecurity Engineer',
  'Frontend Developer',
  'Backend Developer',
  'AI Engineer',
  'Data Scientist',
  'Cloud / DevOps Engineer',
  'iOS Developer',
  'Flutter Developer',
  'Full Stack Developer',
  'Data Engineer',
  'QA / Automation Engineer',
  'UI/UX Designer',
  'Game Developer'
];

export const RoadmapPage: React.FC = () => {
  const { profile } = useProfile();
  const [searchParams, setSearchParams] = useSearchParams();
  const location = useLocation();

  // Query parameter > location state > profile target career > default
  const paramCareer = searchParams.get('career') || (location.state as any)?.career;
  const initialCareer = paramCareer || profile.target_career || 'Android Developer';

  const [selectedCareer, setSelectedCareer] = useState(initialCareer);
  const [duration, setDuration] = useState('6-month');
  const [level, setLevel] = useState('Beginner');
  const [roadmap, setRoadmap] = useState<RoadmapData | null>(null);
  const [loading, setLoading] = useState(false);
  const [activePhase, setActivePhase] = useState(0);
  const [completedSkills, setCompletedSkills] = useState<Record<string, boolean>>({});

  useEffect(() => {
    if (paramCareer) {
      setSelectedCareer(paramCareer);
    }
  }, [paramCareer]);

  const fetchRoadmap = async () => {
    setLoading(true);
    try {
      const data = await apiService.generateRoadmap(selectedCareer, duration, level);
      setRoadmap(data);
      setActivePhase(0);
    } catch (err) {
      console.error('Roadmap generation error:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRoadmap();
    setSearchParams({ career: selectedCareer, duration, level });
  }, [selectedCareer, duration, level]);

  const toggleSkill = (skillKey: string) => {
    setCompletedSkills((prev) => ({
      ...prev,
      [skillKey]: !prev[skillKey],
    }));
  };

  // Compute overall roadmap completion
  const totalSkills = roadmap?.phases.reduce((acc, p) => acc + p.skills_covered.length, 0) || 1;
  const completedCount = Object.values(completedSkills).filter(Boolean).length;
  const completionPercentage = Math.min(Math.round((completedCount / totalSkills) * 100), 100);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-8">
      {/* Top Banner & Control Bar */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 relative overflow-hidden shadow-2xl">
        <div className="absolute top-0 right-0 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none" />

        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6 relative z-10">
          <div>
            <div className="flex items-center space-x-2 text-indigo-400 text-xs font-extrabold uppercase tracking-wider mb-1">
              <Sparkles className="w-4 h-4" />
              <span>Career Execution Engine</span>
            </div>
            <h1 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
              Become a <span className="gradient-text">{selectedCareer}</span>
            </h1>
            <p className="text-slate-400 text-sm mt-1">
              Step-by-step connected progression roadmap, weekly breakdown, practice tasks & milestone projects.
            </p>
          </div>

          {/* Controls Dropdown */}
          <div className="flex flex-wrap items-center gap-2 shrink-0">
            <div>
              <label className="text-[10px] font-bold text-slate-400 uppercase block mb-1">Select Track</label>
              <select
                value={selectedCareer}
                onChange={(e) => setSelectedCareer(e.target.value)}
                className="glass-input px-3.5 py-2.5 rounded-xl text-xs bg-slate-900 font-semibold border border-indigo-500/30 text-white"
              >
                {CAREER_OPTIONS.map((c) => (
                  <option key={c} value={c}>{c}</option>
                ))}
              </select>
            </div>

            <div>
              <label className="text-[10px] font-bold text-slate-400 uppercase block mb-1">Duration</label>
              <select
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
                className="glass-input px-3 py-2.5 rounded-xl text-xs bg-slate-900 border border-white/10"
              >
                <option value="30-day">30-Day Sprint</option>
                <option value="3-month">3-Month Accelerated</option>
                <option value="6-month">6-Month Comprehensive</option>
                <option value="1-year">1-Year Deep Dive</option>
              </select>
            </div>

            <div>
              <label className="text-[10px] font-bold text-slate-400 uppercase block mb-1">Level</label>
              <select
                value={level}
                onChange={(e) => setLevel(e.target.value)}
                className="glass-input px-3 py-2.5 rounded-xl text-xs bg-slate-900 border border-white/10"
              >
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
              </select>
            </div>
          </div>
        </div>

        {/* Roadmap Metadata & Progress Meter */}
        {roadmap && (
          <div className="mt-6 pt-6 border-t border-white/10 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="flex items-center space-x-3 bg-white/5 p-3.5 rounded-2xl border border-white/5">
              <Clock className="w-5 h-5 text-indigo-400 shrink-0" />
              <div>
                <p className="text-[10px] text-slate-400 uppercase font-bold">Weekly Commitment</p>
                <p className="text-xs font-bold text-white">{(roadmap as any).weekly_hours || '10 - 15 hrs / week'}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3 bg-white/5 p-3.5 rounded-2xl border border-white/5">
              <Zap className="w-5 h-5 text-amber-400 shrink-0" />
              <div>
                <p className="text-[10px] text-slate-400 uppercase font-bold">Prerequisites</p>
                <p className="text-xs font-bold text-white truncate max-w-[150px]">{(roadmap as any).prerequisites || 'Basic Logic'}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3 bg-white/5 p-3.5 rounded-2xl border border-white/5">
              <Briefcase className="w-5 h-5 text-emerald-400 shrink-0" />
              <div>
                <p className="text-[10px] text-slate-400 uppercase font-bold">Target Roles</p>
                <p className="text-xs font-bold text-white truncate max-w-[150px]">
                  {((roadmap as any).career_outcomes || [selectedCareer]).join(', ')}
                </p>
              </div>
            </div>

            <div className="flex items-center space-x-3 bg-indigo-600/20 p-3.5 rounded-2xl border border-indigo-500/30">
              <Award className="w-5 h-5 text-indigo-300 shrink-0" />
              <div className="w-full">
                <div className="flex justify-between text-[10px] font-bold text-indigo-300 mb-1">
                  <span>Track Mastery</span>
                  <span>{completionPercentage}%</span>
                </div>
                <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                  <div
                    className="bg-gradient-to-r from-indigo-500 to-purple-500 h-full transition-all duration-500"
                    style={{ width: `${completionPercentage}%` }}
                  />
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {loading ? (
        <div className="glass-panel p-16 rounded-3xl text-center space-y-4 border border-white/10">
          <div className="w-12 h-12 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="text-sm font-semibold text-slate-300">Generating phase progression for {selectedCareer}...</p>
        </div>
      ) : roadmap ? (
        <div className="space-y-8">
          {/* Visual Progression Path Bar */}
          <div className="glass-panel p-4 rounded-3xl border border-white/10 overflow-x-auto no-scrollbar">
            <div className="flex items-center justify-between min-w-[700px] px-2 py-1">
              <div className="flex items-center space-x-2 shrink-0 text-emerald-400 text-xs font-bold uppercase">
                <Target className="w-4 h-4" />
                <span>Start</span>
              </div>

              {roadmap.phases.map((p, pIdx) => (
                <React.Fragment key={pIdx}>
                  <div className="w-8 h-[2px] bg-indigo-500/40" />
                  <button
                    onClick={() => setActivePhase(pIdx)}
                    className={`flex items-center space-x-2 px-3.5 py-2 rounded-2xl text-xs font-bold transition shrink-0 border ${
                      activePhase === pIdx
                        ? 'bg-indigo-600 text-white border-indigo-400 shadow-lg shadow-indigo-500/30'
                        : 'bg-white/5 text-slate-400 border-white/10 hover:text-white hover:bg-white/10'
                    }`}
                  >
                    <span className="w-5 h-5 rounded-full bg-black/30 flex items-center justify-center text-[10px]">
                      0{p.phase_number}
                    </span>
                    <span className="truncate max-w-[110px]">{p.phase_title}</span>
                  </button>
                </React.Fragment>
              ))}

              <div className="w-8 h-[2px] bg-emerald-500/40" />
              <div className="flex items-center space-x-1.5 shrink-0 bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 px-3 py-1.5 rounded-2xl text-xs font-extrabold">
                <Award className="w-4 h-4 text-emerald-400" />
                <span>Job Ready</span>
              </div>
            </div>
          </div>

          {/* Main Grid: Phase Stepper Sidebar + Active Phase Detail */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Left Connected Vertical Steps */}
            <div className="space-y-4">
              <h3 className="text-xs font-bold text-slate-400 uppercase tracking-wider px-1">
                Sequential Progression Steps
              </h3>

              <div className="space-y-3 relative">
                {roadmap.phases.map((phase, pIdx) => (
                  <div
                    key={pIdx}
                    onClick={() => setActivePhase(pIdx)}
                    className={`p-4 rounded-2xl cursor-pointer transition relative border ${
                      activePhase === pIdx
                        ? 'bg-indigo-600/20 border-indigo-500/50 shadow-lg shadow-indigo-500/10'
                        : 'glass-panel border-white/10 hover:border-white/20'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                        Step 0{phase.phase_number}
                      </span>
                      <span className="text-xs text-slate-400 flex items-center gap-1">
                        <Clock className="w-3 h-3 text-indigo-400" /> {phase.duration_weeks} Weeks
                      </span>
                    </div>

                    <h4 className="font-bold text-white text-sm">{phase.phase_title}</h4>

                    <div className="flex flex-wrap gap-1 mt-2">
                      {phase.skills_covered.slice(0, 3).map((skill, sIdx) => (
                        <span key={sIdx} className="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded border border-slate-700">
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Right Detailed Phase Workspace */}
            <div className="lg:col-span-2 space-y-6">
              {roadmap.phases[activePhase] && (
                <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-white/15 space-y-6 shadow-2xl">
                  {/* Phase Header */}
                  <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-4 border-b border-white/10">
                    <div>
                      <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">
                        Phase {roadmap.phases[activePhase].phase_number} of {roadmap.phases.length}
                      </span>
                      <h2 className="text-2xl font-extrabold text-white mt-1">
                        {roadmap.phases[activePhase].phase_title}
                      </h2>
                    </div>

                    <div className="text-xs bg-indigo-500/10 border border-indigo-500/30 px-3 py-1.5 rounded-xl text-indigo-300 font-semibold self-start">
                      Estimated Duration: {roadmap.phases[activePhase].duration_weeks} Weeks
                    </div>
                  </div>

                  {/* Skills Covered Checkboxes */}
                  <div className="space-y-3">
                    <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                      <Code className="w-4 h-4 text-indigo-400" /> Skills to Master (Click to mark complete)
                    </h3>
                    <div className="flex flex-wrap gap-2">
                      {roadmap.phases[activePhase].skills_covered.map((skill, sIdx) => {
                        const skillKey = `${selectedCareer}_P${activePhase}_S${sIdx}`;
                        const isDone = !!completedSkills[skillKey];
                        return (
                          <button
                            key={sIdx}
                            onClick={() => toggleSkill(skillKey)}
                            className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-2 transition border ${
                              isDone
                                ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40'
                                : 'bg-white/5 text-slate-200 border-white/10 hover:border-indigo-500/40'
                            }`}
                          >
                            <CheckCircle2 className={`w-3.5 h-3.5 ${isDone ? 'text-emerald-400' : 'text-slate-500'}`} />
                            <span className={isDone ? 'line-through' : ''}>{skill}</span>
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  {/* Weekly Breakdown */}
                  <div className="space-y-4">
                    <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider">
                      Weekly Curriculum Breakdown
                    </h3>
                    <div className="space-y-3">
                      {roadmap.phases[activePhase].weekly_breakdown.map((w, wIdx) => (
                        <div key={wIdx} className="p-4 rounded-2xl bg-white/5 border border-white/10 space-y-2">
                          <div className="flex items-center justify-between text-xs text-indigo-300 font-bold">
                            <span>Week {w.week}: {w.title}</span>
                          </div>
                          <div className="flex flex-wrap gap-1.5">
                            {w.topics.map((t, tIdx) => (
                              <span key={tIdx} className="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded-lg border border-slate-700">
                                • {t}
                              </span>
                            ))}
                          </div>
                          <p className="text-xs text-emerald-400 font-semibold pt-1">
                            <strong>Practice Task:</strong> {w.practice}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Milestone Project */}
                  <div className="p-5 rounded-2xl bg-gradient-to-r from-purple-950/40 to-indigo-950/40 border border-purple-500/30 flex items-start space-x-3">
                    <CheckCircle2 className="w-6 h-6 text-purple-400 shrink-0 mt-0.5" />
                    <div>
                      <h4 className="text-xs font-bold text-purple-300 uppercase">Phase Milestone Project</h4>
                      <p className="text-sm font-bold text-white mt-1">
                        {roadmap.phases[activePhase].milestone_project}
                      </p>
                      <p className="text-xs text-slate-400 mt-1">
                        Build this project and push the source code to GitHub with a detailed README to validate Phase {roadmap.phases[activePhase].phase_number} completion.
                      </p>
                    </div>
                  </div>

                  {/* Resources */}
                  <div className="space-y-3 pt-2 border-t border-white/10">
                    <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                      <BookOpen className="w-4 h-4 text-indigo-400" /> Recommended Phase Learning Resources
                    </h3>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      {roadmap.phases[activePhase].learning_resources.map((res, rIdx) => (
                        <a
                          key={rIdx}
                          href={res.url}
                          target="_blank"
                          rel="noreferrer"
                          className="p-3.5 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/10 flex items-center justify-between text-xs text-slate-200 transition group"
                        >
                          <div className="space-y-1 truncate pr-2">
                            <span className="font-bold text-white group-hover:text-indigo-300 truncate block">
                              {res.title}
                            </span>
                            <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300">
                              {res.badge}
                            </span>
                          </div>
                          <ExternalLink className="w-4 h-4 text-indigo-400 shrink-0 ml-2" />
                        </a>
                      ))}
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
