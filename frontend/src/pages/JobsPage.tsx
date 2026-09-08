import React, { useState, useEffect } from 'react';
import { Briefcase, ExternalLink, ShieldAlert, CheckCircle2 } from 'lucide-react';
import { apiService } from '../services/api';

export const JobsPage: React.FC = () => {
  const [jobsData, setJobsData] = useState<any>(null);

  useEffect(() => {
    apiService.getJobs().then(setJobsData).catch(console.error);
  }, []);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      {/* Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20">
        <div className="flex items-center space-x-3 mb-1">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <Briefcase className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Job & Internship Guidance</h1>
            <p className="text-slate-400 text-sm">
              Legitimate hiring portals for freshers, experienced professionals, and remote roles.
            </p>
          </div>
        </div>
      </div>

      {jobsData && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Legitimate Platforms Grid */}
          <div className="lg:col-span-2 space-y-4">
            <h2 className="text-base font-bold text-white">Verified Hiring Portals</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {jobsData.platforms.map((platform: any, idx: number) => (
                <div
                  key={idx}
                  className="glass-panel glass-panel-hover p-5 rounded-2xl border border-white/10 flex flex-col justify-between space-y-3"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                      {platform.category}
                    </span>
                    <a
                      href={platform.url}
                      target="_blank"
                      rel="noreferrer"
                      className="p-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-indigo-400"
                    >
                      <ExternalLink className="w-4 h-4" />
                    </a>
                  </div>
                  <div>
                    <h3 className="font-bold text-white text-base">{platform.name}</h3>
                    <p className="text-xs text-slate-400 mt-1">{platform.description}</p>
                  </div>
                  <div className="pt-2 border-t border-white/5 flex items-center gap-1 text-[11px] text-emerald-400 font-semibold">
                    <CheckCircle2 className="w-3.5 h-3.5" /> 100% Free Candidate Access
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Job Scam Protection Rules */}
          <div className="glass-panel p-6 rounded-3xl border border-rose-500/30 space-y-4">
            <div className="flex items-center space-x-2 text-rose-400">
              <ShieldAlert className="w-5 h-5" />
              <h3 className="font-bold text-white text-base">Job Scam Warnings</h3>
            </div>

            <div className="space-y-3 text-xs text-slate-300">
              {jobsData.scam_warnings.map((rule: string, idx: number) => (
                <div key={idx} className="p-3 rounded-xl bg-rose-950/20 border border-rose-500/20">
                  {rule}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
