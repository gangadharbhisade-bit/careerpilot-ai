import React, { useState } from 'react';
import { FileText, Sparkles, CheckCircle, AlertTriangle, ArrowRight, Upload } from 'lucide-react';
import { apiService } from '../services/api';
import { ResumeAnalysisData } from '../types';
import { useProfile } from '../context/ProfileContext';

export const ResumePage: React.FC = () => {
  const { profile } = useProfile();
  const [targetRole, setTargetRole] = useState(profile.target_career || 'Software Developer');
  const [resumeText, setResumeText] = useState(
    `Experienced Python developer with a strong foundation in SQL, Data Structures, and Web Development. Built REST APIs using FastAPI and frontends with React. Worked on machine learning models and dataset analysis.`
  );
  const [analysis, setAnalysis] = useState<ResumeAnalysisData | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!resumeText.trim()) return;
    setLoading(true);
    try {
      const result = await apiService.analyzeResume(targetRole, resumeText);
      setAnalysis(result);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      {/* Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20">
        <div className="flex items-center space-x-3 mb-1">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <FileText className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Resume Guidance & ATS Analyzer</h1>
            <p className="text-slate-400 text-sm">
              Review your resume content, evaluate ATS keyword matching, and transform bullet points.
            </p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column: Text Input & Target Role */}
        <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
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
            </select>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase tracking-wider block mb-2">
              Paste Resume Content / Project Descriptions
            </label>
            <textarea
              rows={10}
              value={resumeText}
              onChange={(e) => setResumeText(e.target.value)}
              placeholder="Paste your resume text or bullet points here..."
              className="glass-input w-full p-3 rounded-xl text-xs bg-slate-900 text-slate-200 resize-none font-mono"
            />
          </div>

          <button
            onClick={handleAnalyze}
            disabled={loading}
            className="gradient-btn w-full py-3 rounded-xl text-xs font-bold text-white uppercase tracking-wider flex items-center justify-center space-x-2 disabled:opacity-50"
          >
            <Sparkles className="w-4 h-4" />
            <span>{loading ? 'Analyzing...' : 'Run ATS Audit'}</span>
          </button>
        </div>

        {/* Right Column: ATS Score & Bullet Point Improver */}
        <div className="lg:col-span-2 space-y-6">
          {analysis ? (
            <>
              {/* ATS Score Overview */}
              <div className="glass-panel p-6 rounded-3xl border border-white/10 flex flex-col sm:flex-row items-center justify-between gap-6">
                <div>
                  <h3 className="text-xs font-bold text-indigo-400 uppercase">Estimated ATS Score</h3>
                  <h2 className="text-3xl font-extrabold text-white mt-1">
                    {analysis.ats_score} / 100
                  </h2>
                  <p className="text-xs text-slate-400 mt-1">
                    Matched {analysis.matched_keywords.length} core keywords for {targetRole}.
                  </p>
                </div>

                <div className="flex flex-wrap gap-1.5 max-w-xs">
                  {analysis.matched_keywords.map((kw, idx) => (
                    <span key={idx} className="text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2.5 py-0.5 rounded-full">
                      ✓ {kw}
                    </span>
                  ))}
                  {analysis.missing_keywords.map((kw, idx) => (
                    <span key={idx} className="text-[10px] bg-rose-500/20 text-rose-300 border border-rose-500/30 px-2.5 py-0.5 rounded-full">
                      ✗ {kw}
                    </span>
                  ))}
                </div>
              </div>

              {/* Bullet Point Rewriter */}
              <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-4">
                <h3 className="text-sm font-bold text-slate-200">
                  Impact-Driven Bullet Point Suggestions
                </h3>
                <div className="space-y-3">
                  {analysis.suggested_bullet_points.map((item, idx) => (
                    <div key={idx} className="p-4 rounded-2xl bg-white/5 border border-white/10 space-y-2">
                      <p className="text-xs text-slate-400 line-through">
                        <strong>Before:</strong> "{item.original}"
                      </p>
                      <p className="text-xs text-emerald-300 font-semibold">
                        <strong>Improved:</strong> "{item.improved}"
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            </>
          ) : (
            <div className="glass-panel p-12 rounded-3xl text-center text-slate-400 space-y-2 border border-white/10">
              <FileText className="w-12 h-12 text-slate-600 mx-auto" />
              <p className="text-sm font-medium">Click "Run ATS Audit" to receive instant feedback.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
