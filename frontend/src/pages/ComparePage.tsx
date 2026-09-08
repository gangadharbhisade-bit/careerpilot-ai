import React, { useState, useEffect } from 'react';
import { GitCompare, Sparkles, CheckCircle2 } from 'lucide-react';
import { apiService } from '../services/api';

export const ComparePage: React.FC = () => {
  const [careerA, setCareerA] = useState('Data Scientist');
  const [careerB, setCareerB] = useState('AI Engineer');
  const [comparison, setComparison] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const fetchComparison = async () => {
    setLoading(true);
    try {
      const res = await apiService.compareCareers(careerA, careerB);
      setComparison(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchComparison();
  }, [careerA, careerB]);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      {/* Title */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <GitCompare className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Career Comparison Matrix</h1>
            <p className="text-slate-400 text-sm">
              Compare skills, daily work, salary realities, and learning curves side-by-side.
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <select
            value={careerA}
            onChange={(e) => setCareerA(e.target.value)}
            className="glass-input px-3 py-2 rounded-xl text-xs bg-slate-900 border border-white/15"
          >
            <option value="Data Scientist">Data Scientist</option>
            <option value="Frontend Developer">Frontend Developer</option>
            <option value="AI Engineer">AI Engineer</option>
          </select>
          <span className="text-xs text-indigo-400 font-bold">VS</span>
          <select
            value={careerB}
            onChange={(e) => setCareerB(e.target.value)}
            className="glass-input px-3 py-2 rounded-xl text-xs bg-slate-900 border border-white/15"
          >
            <option value="AI Engineer">AI Engineer</option>
            <option value="Full Stack Developer">Full Stack Developer</option>
            <option value="Data Scientist">Data Scientist</option>
          </select>
        </div>
      </div>

      {comparison && (
        <div className="space-y-6">
          {/* Summary Card */}
          <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-3">
            <h3 className="text-xs font-bold text-indigo-400 uppercase">Executive Overview</h3>
            <p className="text-sm text-slate-200 leading-relaxed">{comparison.summary}</p>
          </div>

          {/* Comparison Matrix Table */}
          <div className="glass-panel rounded-3xl border border-white/10 overflow-hidden">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="bg-white/5 border-b border-white/10 text-indigo-300 font-bold uppercase text-[11px]">
                  <th className="p-4">Metric / Dimension</th>
                  <th className="p-4 bg-indigo-600/10 border-l border-white/10 text-white">{comparison.career_a}</th>
                  <th className="p-4 bg-purple-600/10 border-l border-white/10 text-white">{comparison.career_b}</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/5 text-slate-300">
                {comparison.comparison_table.map((row: any, idx: number) => (
                  <tr key={idx} className="hover:bg-white/5 transition">
                    <td className="p-4 font-semibold text-white">{row.metric_name}</td>
                    <td className="p-4 border-l border-white/10 bg-indigo-950/10">{row.career_a_value}</td>
                    <td className="p-4 border-l border-white/10 bg-purple-950/10">{row.career_b_value}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Verdict Guidance */}
          <div className="glass-panel p-6 rounded-3xl border border-emerald-500/30 bg-emerald-950/10 flex items-start space-x-3">
            <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
            <div>
              <h4 className="text-xs font-bold text-emerald-400 uppercase">Counselor Verdict & Recommendation</h4>
              <p className="text-sm text-white mt-1">{comparison.verdict_guidance}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
