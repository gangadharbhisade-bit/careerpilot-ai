import React, { useState, useEffect } from 'react';
import { Building2, ExternalLink, Search, Sparkles } from 'lucide-react';
import { apiService } from '../services/api';
import { useProfile } from '../context/ProfileContext';

export const CompanyPage: React.FC = () => {
  const { profile } = useProfile();
  const [career, setCareer] = useState(profile.target_career || 'AI Engineer');
  const [companies, setCompanies] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchCompanies = async () => {
    setLoading(true);
    try {
      const res = await apiService.getTargetCompanies(career);
      setCompanies(res.companies || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCompanies();
  }, [career]);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <Building2 className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Target Companies Engine</h1>
            <p className="text-slate-400 text-sm">
              Discover top hiring companies, key tech focus, and direct official career portals.
            </p>
          </div>
        </div>

        <select
          value={career}
          onChange={(e) => setCareer(e.target.value)}
          className="glass-input px-4 py-2.5 rounded-xl text-sm bg-slate-900 border border-white/10"
        >
          <option value="AI Engineer">AI Engineer</option>
          <option value="Software Developer">Software Developer</option>
          <option value="Data Scientist">Data Scientist</option>
          <option value="Cybersecurity Engineer">Cybersecurity Engineer</option>
          <option value="Cloud/DevOps Engineer">Cloud/DevOps Engineer</option>
        </select>
      </div>

      {loading ? (
        <div className="text-center p-12 glass-panel rounded-3xl text-slate-300">
          Fetching target companies for {career}...
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {companies.map((company, idx) => (
            <div
              key={idx}
              className="glass-panel glass-panel-hover p-6 rounded-3xl border border-white/10 flex flex-col justify-between space-y-4"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30">
                    {company.type}
                  </span>
                  <a
                    href={company.careers_url}
                    target="_blank"
                    rel="noreferrer"
                    className="p-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-indigo-400"
                    title="Official Careers Portal"
                  >
                    <ExternalLink className="w-4 h-4" />
                  </a>
                </div>
                <h3 className="font-bold text-white text-lg">{company.name}</h3>
                <p className="text-xs text-slate-400 mt-2">
                  <strong className="text-indigo-300">Tech Focus:</strong> {company.focus}
                </p>
              </div>

              <a
                href={company.careers_url}
                target="_blank"
                rel="noreferrer"
                className="gradient-btn w-full py-2.5 rounded-xl text-xs font-bold text-white text-center block"
              >
                Apply via Official Portal
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
