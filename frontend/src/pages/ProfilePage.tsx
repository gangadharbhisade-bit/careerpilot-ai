import React, { useState } from 'react';
import { UserCheck, Save, Sparkles, CheckCircle2 } from 'lucide-react';
import { useProfile } from '../context/ProfileContext';

export const ProfilePage: React.FC = () => {
  const { profile, updateProfile } = useProfile();
  const [formData, setFormData] = useState(profile);
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    updateProfile(formData);
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 3000);
  };

  return (
    <div className="p-4 sm:p-8 max-w-4xl mx-auto space-y-6">
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <UserCheck className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Personalized Career Profile</h1>
            <p className="text-slate-400 text-sm">
              Keep your profile updated so the AI Counselor customizes every roadmap & response.
            </p>
          </div>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="glass-panel p-6 sm:p-8 rounded-3xl border border-white/10 space-y-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Target Career Role</label>
            <input
              type="text"
              value={formData.target_career}
              onChange={(e) => setFormData({ ...formData, target_career: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm"
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Current Role / Status</label>
            <input
              type="text"
              value={formData.current_role}
              onChange={(e) => setFormData({ ...formData, current_role: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm"
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Education Degree</label>
            <input
              type="text"
              value={formData.degree}
              onChange={(e) => setFormData({ ...formData, degree: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm"
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Branch / Major</label>
            <input
              type="text"
              value={formData.branch}
              onChange={(e) => setFormData({ ...formData, branch: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm"
            />
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Experience Level</label>
            <select
              value={formData.experience_level}
              onChange={(e) => setFormData({ ...formData, experience_level: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm bg-slate-900"
            >
              <option value="Beginner">Beginner (0 - 1 year)</option>
              <option value="Intermediate">Intermediate (1 - 3 years)</option>
              <option value="Advanced">Advanced (3+ years)</option>
            </select>
          </div>

          <div>
            <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Available Learning Time</label>
            <select
              value={formData.available_learning_time}
              onChange={(e) => setFormData({ ...formData, available_learning_time: e.target.value })}
              className="glass-input w-full p-3 rounded-xl text-sm bg-slate-900"
            >
              <option value="30 min/day">30 minutes / day</option>
              <option value="1 hour/day">1 hour / day</option>
              <option value="2 hours/day">2 hours / day</option>
              <option value="4 hours/day">4 hours / day</option>
            </select>
          </div>
        </div>

        <div>
          <label className="text-xs font-bold text-slate-300 uppercase block mb-1">Long Term Career Goal Statement</label>
          <textarea
            rows={3}
            value={formData.career_goal}
            onChange={(e) => setFormData({ ...formData, career_goal: e.target.value })}
            className="glass-input w-full p-3 rounded-xl text-sm resize-none"
          />
        </div>

        <div className="flex items-center justify-between pt-4 border-t border-white/10">
          {savedSuccess ? (
            <span className="text-xs text-emerald-400 font-bold flex items-center gap-1">
              <CheckCircle2 className="w-4 h-4" /> Career Profile Updated Successfully!
            </span>
          ) : (
            <span className="text-xs text-slate-400">All responses are saved to personalize your AI counselor.</span>
          )}

          <button
            type="submit"
            className="gradient-btn px-6 py-3 rounded-xl text-xs font-bold text-white flex items-center space-x-2"
          >
            <Save className="w-4 h-4" />
            <span>Save Profile</span>
          </button>
        </div>
      </form>
    </div>
  );
};
