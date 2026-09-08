import React from 'react';
import { ShieldAlert, X, AlertTriangle, CheckCircle2 } from 'lucide-react';

interface ScamAlertModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const ScamAlertModal: React.FC<ScamAlertModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-md p-4">
      <div className="bg-[#111622] border border-rose-500/30 rounded-2xl p-6 max-w-lg w-full shadow-2xl relative animate-in fade-in zoom-in-95">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-slate-400 hover:text-white p-1 rounded-lg bg-white/5"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center space-x-3 mb-4 text-rose-400">
          <div className="p-3 bg-rose-500/20 rounded-xl border border-rose-500/30">
            <ShieldAlert className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">Job Scam Protection Guide</h3>
            <p className="text-xs text-rose-300">Stay safe while applying for jobs & internships</p>
          </div>
        </div>

        <div className="space-y-3 text-xs text-slate-300 bg-rose-950/20 p-4 rounded-xl border border-rose-500/20 mb-5">
          <div className="flex items-start space-x-2">
            <AlertTriangle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
            <p><strong className="text-white">Never pay for job offers:</strong> Legitimate companies NEVER charge candidates for application fees, laptops, training bonds, or security deposits.</p>
          </div>

          <div className="flex items-start space-x-2">
            <AlertTriangle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
            <p><strong className="text-white">Verify Email Domains:</strong> Ensure job correspondence comes from official domains (e.g. @microsoft.com or @google.com), not free @gmail.com or @yahoo.com accounts.</p>
          </div>

          <div className="flex items-start space-x-2">
            <AlertTriangle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
            <p><strong className="text-white">No Money Transfers:</strong> Beware of fake cheque scams or requests to transfer money during interview stages.</p>
          </div>
        </div>

        <div className="flex justify-end">
          <button
            onClick={onClose}
            className="flex items-center space-x-2 bg-gradient-to-r from-rose-600 to-indigo-600 hover:from-rose-500 hover:to-indigo-500 text-white text-xs font-semibold py-2 px-5 rounded-xl shadow-lg transition"
          >
            <CheckCircle2 className="w-4 h-4" />
            <span>I Understand & Agree</span>
          </button>
        </div>
      </div>
    </div>
  );
};
