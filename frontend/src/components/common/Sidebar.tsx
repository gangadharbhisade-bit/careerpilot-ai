import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  MessageSquareCode,
  Map,
  Compass,
  BookOpen,
  Briefcase,
  Building2,
  FileText,
  Video,
  GitCompare,
  CheckSquare,
  UserCheck,
  Sparkles,
  ShieldAlert
} from 'lucide-react';

interface SidebarProps {
  isOpen: boolean;
  onClose?: () => void;
  onOpenScamAlert: () => void;
}

const navItems = [
  { name: 'Dashboard', path: '/app/dashboard', icon: LayoutDashboard },
  { name: 'AI Career Chat', path: '/app/chat', icon: MessageSquareCode, badge: 'AI' },
  { name: 'Career Roadmaps', path: '/app/roadmaps', icon: Map },
  { name: 'Skill Gap Analyzer', path: '/app/skill-gap', icon: Compass },
  { name: 'Learning Resources', path: '/app/resources', icon: BookOpen },
  { name: 'Job & Internships', path: '/app/jobs', icon: Briefcase },
  { name: 'Target Companies', path: '/app/companies', icon: Building2 },
  { name: 'Resume Assistant', path: '/app/resume', icon: FileText },
  { name: 'Mock Interview Prep', path: '/app/interview', icon: Video },
  { name: 'Career Comparison', path: '/app/compare', icon: GitCompare },
  { name: 'Daily Planner', path: '/app/planner', icon: CheckSquare },
  { name: 'My Profile', path: '/app/profile', icon: UserCheck },
];

export const Sidebar: React.FC<SidebarProps> = ({ isOpen, onClose, onOpenScamAlert }) => {
  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
          onClick={onClose}
        />
      )}

      <aside
        className={`fixed top-0 left-0 bottom-0 w-64 bg-[#0e131f]/95 backdrop-blur-xl border-r border-white/10 z-50 transition-transform duration-300 flex flex-col justify-between ${
          isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        }`}
      >
        <div>
          {/* Logo Header */}
          <div className="p-5 border-b border-white/10 flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="font-extrabold text-lg text-white tracking-wide">
                  Career<span className="text-indigo-400">Pilot</span> <span className="text-xs bg-indigo-500/20 text-indigo-300 px-1.5 py-0.5 rounded border border-indigo-500/30">AI</span>
                </h1>
                <p className="text-[10px] text-slate-400">Intelligent Counselor</p>
              </div>
            </div>
          </div>

          {/* Navigation Links */}
          <nav className="p-3 space-y-1 overflow-y-auto max-h-[calc(100vh-180px)]">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.path}
                  to={item.path}
                  onClick={onClose}
                  className={({ isActive }) =>
                    `flex items-center justify-between px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all ${
                      isActive
                        ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/40 shadow-inner'
                        : 'text-slate-400 hover:text-white hover:bg-white/5'
                    }`
                  }
                >
                  <div className="flex items-center space-x-3">
                    <Icon className="w-4 h-4" />
                    <span>{item.name}</span>
                  </div>
                  {item.badge && (
                    <span className="text-[10px] bg-purple-500/20 text-purple-300 border border-purple-500/30 px-1.5 py-0.5 rounded-full font-bold">
                      {item.badge}
                    </span>
                  )}
                </NavLink>
              );
            })}
          </nav>
        </div>

        {/* Footer Security Badge */}
        <div className="p-4 border-t border-white/10 bg-indigo-950/20">
          <button
            onClick={onOpenScamAlert}
            className="w-full flex items-center justify-center space-x-2 bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/30 text-rose-300 text-xs font-semibold py-2 px-3 rounded-xl transition-all"
          >
            <ShieldAlert className="w-4 h-4 text-rose-400" />
            <span>Job Scam Warning</span>
          </button>
        </div>
      </aside>
    </>
  );
};
