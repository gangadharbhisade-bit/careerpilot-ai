import React, { useState, useEffect } from 'react';
import { BookOpen, ExternalLink, ShieldCheck, Video, Code } from 'lucide-react';
import { apiService } from '../services/api';

export const ResourcesPage: React.FC = () => {
  const [resources, setResources] = useState<any>(null);

  useEffect(() => {
    apiService.getResources().then(setResources).catch(console.error);
  }, []);

  return (
    <div className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6">
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20">
        <div className="flex items-center space-x-3 mb-1">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <BookOpen className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Verified Learning Resources</h1>
            <p className="text-slate-400 text-sm">
              Curated official documentation, interactive practice platforms, and top video courses.
            </p>
          </div>
        </div>
      </div>

      {resources && (
        <div className="space-y-8">
          {/* Official Documentation */}
          <div className="space-y-4">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-indigo-400" /> Official Documentation
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              {resources.official_docs.map((res: any, idx: number) => (
                <a
                  key={idx}
                  href={res.url}
                  target="_blank"
                  rel="noreferrer"
                  className="glass-panel glass-panel-hover p-4 rounded-2xl border border-white/10 flex flex-col justify-between space-y-3"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                      {res.badge}
                    </span>
                    <ExternalLink className="w-4 h-4 text-slate-400" />
                  </div>
                  <h3 className="font-bold text-white text-sm">{res.title}</h3>
                  <p className="text-xs text-slate-400">Authoritative reference manual</p>
                </a>
              ))}
            </div>
          </div>

          {/* Interactive Platforms */}
          <div className="space-y-4">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <Code className="w-5 h-5 text-purple-400" /> Interactive Practice & Coding
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {resources.interactive_platforms.map((res: any, idx: number) => (
                <a
                  key={idx}
                  href={res.url}
                  target="_blank"
                  rel="noreferrer"
                  className="glass-panel glass-panel-hover p-5 rounded-2xl border border-white/10 flex flex-col justify-between space-y-3"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                      {res.category}
                    </span>
                    <ExternalLink className="w-4 h-4 text-indigo-400" />
                  </div>
                  <h3 className="font-bold text-white text-base">{res.title}</h3>
                  <p className="text-xs text-slate-400">Hands-on interactive exercises & challenges</p>
                </a>
              ))}
            </div>
          </div>

          {/* Top Video Courses */}
          <div className="space-y-4">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <Video className="w-5 h-5 text-cyan-400" /> Video & Certificate Courses
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {resources.top_video_courses.map((res: any, idx: number) => (
                <a
                  key={idx}
                  href={res.url}
                  target="_blank"
                  rel="noreferrer"
                  className="glass-panel glass-panel-hover p-5 rounded-2xl border border-white/10 flex flex-col justify-between space-y-3"
                >
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/30">
                      {res.badge}
                    </span>
                    <ExternalLink className="w-4 h-4 text-cyan-400" />
                  </div>
                  <h3 className="font-bold text-white text-base">{res.title}</h3>
                  <p className="text-xs text-slate-400">Comprehensive video lectures & projects</p>
                </a>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
