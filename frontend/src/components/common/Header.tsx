import React from 'react';
import { Menu, User, ShieldAlert, Sparkles } from 'lucide-react';
import { useProfile } from '../../context/ProfileContext';
import { useAuth } from '../../context/AuthContext';

interface HeaderProps {
  onToggleSidebar: () => void;
  onOpenScamAlert: () => void;
}

export const Header: React.FC<HeaderProps> = ({ onToggleSidebar, onOpenScamAlert }) => {
  const { profile } = useProfile();
  const { user } = useAuth();

  return (
    <header className="sticky top-0 z-30 bg-[#0e131f]/80 backdrop-blur-md border-b border-white/10 px-4 py-3 flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <button
          onClick={onToggleSidebar}
          className="p-2 rounded-lg bg-white/5 hover:bg-white/10 text-slate-300 lg:hidden"
        >
          <Menu className="w-5 h-5" />
        </button>

        {/* Current Target Goal Badge */}
        <div className="hidden sm:flex items-center space-x-2 bg-indigo-500/10 border border-indigo-500/30 px-3 py-1 rounded-full text-xs text-indigo-300">
          <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
          <span>Goal: <strong className="text-white">{profile.target_career || 'Not Set'}</strong></span>
        </div>
      </div>

      {/* Right controls */}
      <div className="flex items-center space-x-3">
        {/* Scam warning button */}
        <button
          onClick={onOpenScamAlert}
          className="hidden md:flex items-center space-x-1.5 bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 text-xs px-3 py-1.5 rounded-lg border border-rose-500/30 font-medium transition"
        >
          <ShieldAlert className="w-3.5 h-3.5" />
          <span>Scam Shield</span>
        </button>

        {/* AI Engine Status indicator */}
        <div className="flex items-center space-x-2 bg-emerald-500/10 border border-emerald-500/30 px-2.5 py-1 rounded-full text-[11px] text-emerald-400">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>AI Active</span>
        </div>

        {/* User profile avatar */}
        <div className="flex items-center space-x-2 bg-white/5 border border-white/10 px-3 py-1.5 rounded-xl">
          <div className="w-6 h-6 rounded-full bg-indigo-600 flex items-center justify-center text-xs font-bold text-white">
            {user?.full_name ? user.full_name.charAt(0) : 'U'}
          </div>
          <span className="text-xs text-slate-200 font-medium hidden sm:inline">
            {user?.full_name || 'User Navigator'}
          </span>
        </div>
      </div>
    </header>
  );
};
