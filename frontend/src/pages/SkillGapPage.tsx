import React, { useState, useEffect } from 'react';
import { Compass, CheckCircle, XCircle, Plus, Trash2, ArrowRight, BookOpen, Clock } from 'lucide-react';
import { apiService } from '../services/api';
import { SkillGapData } from '../types';
import { useProfile } from '../context/ProfileContext';

export const SkillGapPage: React.FC = () => {
  const { profile } = useProfile();
  const [currentSkills, setCurrentSkills] = useState<string[]>(profile.skills || ['Python', 'SQL']);
  const [newSkillInput, setNewSkillInput] = useState('');
  const [targetRole, setTargetRole] = useState(profile.target_career || 'AI Engineer');
  const [gapData, setGapData] = useState<SkillGapData | null>(null);
  const [loading, setLoading] = useState(false);

  const runAnalysis = async () => {
    setLoading(true);
    try {
      const data = await apiService.analyzeSkillGap(currentSkills, targetRole);
      setGapData(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    runAnalysis();
  }, [targetRole]);

  const addSkill = () => {
    if (newSkillInput.trim() && !currentSkills.includes(newSkillInput.trim())) {
      const updated = [...currentSkills, newSkillInput.trim()];
      setCurrentSkills(updated);
      setNewSkillInput('');
    }
  };

  const removeSkill = (skillToRemove: string) => {
    setCurrentSkills(currentSkills.filter((s) => s !== skillToRemove));
  };

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      {/* Title Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20">
        <div className="flex items-center space-x-3 mb-2">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <Compass className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Skill Gap Analyzer</h1>
            <p className="text-slate-400 text-sm">
              Compare your current skill inventory against target market requirements.
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column: Skill Inventory Controls */}
        <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-5">
          <div>
            <label className="text-xs font-bold text-slate-300 uppercase tracking-wider block mb-2">
              Target Career Role
            </label>
            <select
              value={targetRole}
              onChange={(e) => setTargetRole(e.target.value)}
              className="glass-input w-full p-3 rounded-xl text-sm bg-slate-900 border border-white/15"
            >
              <option value="AI Engineer">AI Engineer</option>
              <option value="Software Developer">Software Developer</option>
              <option value="Data Scientist">Data Scientist</option>
              <option value="Cybersecurity Engineer">Cybersecurity Engineer</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase tracking-wider block mb-2">
              Your Current Skills
            </label>

            <div className="flex items-center space-x-2 mb-3">
              <input
                type="text"
                value={newSkillInput}
                onChange={(e) => setNewSkillInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && addSkill()}
                placeholder="Add skill (e.g. PyTorch, React)..."
                className="glass-input flex-1 p-2.5 rounded-xl text-xs bg-slate-900"
              />
              <button
                onClick={addSkill}
                className="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white transition"
              >
                <Plus className="w-4 h-4" />
              </button>
            </div>

            <div className="flex flex-wrap gap-2 max-h-48 overflow-y-auto pr-1">
              {currentSkills.map((skill, idx) => (
                <span
                  key={idx}
                  className="bg-indigo-600/20 text-indigo-200 border border-indigo-500/30 px-3 py-1 rounded-full text-xs flex items-center gap-1.5"
                >
                  {skill}
                  <button onClick={() => removeSkill(skill)} className="hover:text-rose-400">
                    <Trash2 className="w-3 h-3" />
                  </button>
                </span>
              ))}
            </div>
          </div>

          <button
            onClick={runAnalysis}
            className="gradient-btn w-full py-3 rounded-xl text-xs font-bold text-white uppercase tracking-wider flex items-center justify-center space-x-2"
          >
            <span>Recalculate Gap</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>

        {/* Right Column: Readiness Score & Gap Results */}
        <div className="lg:col-span-2 space-y-6">
          {gapData && (
            <>
              {/* Readiness Score Card */}
              <div className="glass-panel p-6 rounded-3xl border border-white/10 flex flex-col sm:flex-row items-center justify-between gap-6">
                <div>
                  <h3 className="text-xs font-bold text-indigo-400 uppercase">Role Readiness Meter</h3>
                  <h2 className="text-2xl font-bold text-white mt-1">
                    {gapData.target_role} Match
                  </h2>
                  <p className="text-xs text-slate-400 mt-1">
                    Matched {gapData.required_skills.length - gapData.missing_skills.length} out of {gapData.required_skills.length} core market skills.
                  </p>
                </div>

                {/* Score Circle Gauge */}
                <div className="relative w-28 h-28 flex items-center justify-center shrink-0">
                  <svg className="w-full h-full transform -rotate-90">
                    <circle
                      cx="56"
                      cy="56"
                      r="45"
                      className="text-slate-800"
                      strokeWidth="10"
                      stroke="currentColor"
                      fill="transparent"
                    />
                    <circle
                      cx="56"
                      cy="56"
                      r="45"
                      className="text-indigo-500 transition-all duration-1000"
                      strokeWidth="10"
                      strokeDasharray={282}
                      strokeDashoffset={282 - (282 * gapData.readiness_percentage) / 100}
                      strokeLinecap="round"
                      stroke="currentColor"
                      fill="transparent"
                    />
                  </svg>
                  <span className="absolute text-xl font-extrabold text-white">
                    {gapData.readiness_percentage}%
                  </span>
                </div>
              </div>

              {/* Missing Skills Priority List */}
              <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
                <h3 className="text-sm font-bold text-slate-200">
                  Missing Skill Priority & Learning Estimate
                </h3>

                <div className="space-y-3">
                  {gapData.priority_order.map((item, idx) => (
                    <div
                      key={idx}
                      className="p-4 rounded-2xl bg-white/5 border border-white/10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3"
                    >
                      <div className="space-y-1">
                        <div className="flex items-center space-x-2">
                          <span className="font-bold text-white text-sm">{item.skill}</span>
                          <span
                            className={`text-[10px] font-extrabold px-2 py-0.5 rounded-full ${
                              item.priority === 'CRITICAL'
                                ? 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                                : 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                            }`}
                          >
                            {item.priority}
                          </span>
                        </div>
                        <p className="text-xs text-slate-400 flex items-center gap-1">
                          <BookOpen className="w-3 h-3 text-indigo-400" /> Resource: {item.resource}
                        </p>
                      </div>

                      <div className="text-xs text-slate-300 bg-slate-800/80 px-3 py-1.5 rounded-xl border border-slate-700 flex items-center gap-1.5 shrink-0">
                        <Clock className="w-3.5 h-3.5 text-indigo-400" />
                        <span>~{item.hours} hours needed</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
