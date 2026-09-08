import React, { useState } from 'react';
import { Video, Send, CheckCircle2, Award, Sparkles, RefreshCw, AlertCircle } from 'lucide-react';
import { apiService } from '../services/api';
import { InterviewTurn } from '../types';
import { useProfile } from '../context/ProfileContext';

export const InterviewPage: React.FC = () => {
  const { profile } = useProfile();
  const [targetRole, setTargetRole] = useState(profile.target_career || 'Software Developer');
  const [interviewType, setInterviewType] = useState('Technical');
  const [session, setSession] = useState<InterviewTurn | null>(null);
  const [userAnswer, setUserAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const startNewInterview = async () => {
    setLoading(true);
    try {
      const res = await apiService.startInterview(targetRole, interviewType);
      setSession(res);
      setUserAnswer('');
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleAnswerSubmit = async () => {
    if (!session || !userAnswer.trim()) return;
    setLoading(true);
    try {
      const res = await apiService.submitInterviewAnswer(session.session_id, userAnswer);
      setSession(res);
      setUserAnswer('');
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 sm:p-8 max-w-5xl mx-auto space-y-6">
      {/* Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <Video className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">AI Mock Interview Prep</h1>
            <p className="text-slate-400 text-sm">
              Practice turn-by-turn interview simulation with real-time AI scoring & sample improvements.
            </p>
          </div>
        </div>

        {!session && (
          <div className="flex items-center gap-2">
            <select
              value={interviewType}
              onChange={(e) => setInterviewType(e.target.value)}
              className="glass-input px-3 py-2 rounded-xl text-xs bg-slate-900 border border-white/15"
            >
              <option value="Technical">Technical Interview</option>
              <option value="HR">HR / General Interview</option>
              <option value="System Design">System Design</option>
            </select>

            <button
              onClick={startNewInterview}
              disabled={loading}
              className="gradient-btn px-4 py-2 rounded-xl text-xs font-bold text-white flex items-center space-x-1.5"
            >
              <Sparkles className="w-4 h-4" />
              <span>Start Mock Session</span>
            </button>
          </div>
        )}
      </div>

      {session ? (
        <div className="space-y-6">
          {/* Question Card */}
          <div className="glass-panel p-6 rounded-3xl border border-indigo-500/30 relative">
            <div className="flex items-center justify-between mb-3">
              <span className="text-xs font-extrabold uppercase tracking-wider text-indigo-400 px-3 py-1 bg-indigo-500/20 rounded-full border border-indigo-500/30">
                Question {session.question_number}
              </span>
              <button
                onClick={() => setSession(null)}
                className="text-xs text-slate-400 hover:text-white flex items-center gap-1"
              >
                <RefreshCw className="w-3.5 h-3.5" /> End Session
              </button>
            </div>
            <h2 className="text-xl font-bold text-white leading-relaxed">
              {session.question}
            </h2>
          </div>

          {/* Feedback on Previous Answer if available */}
          {session.previous_evaluation && (
            <div className="glass-panel p-6 rounded-3xl border border-white/10 space-y-3 bg-indigo-950/20">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-slate-400 uppercase">Previous Question Feedback</span>
                <span className="text-sm font-extrabold text-emerald-400 bg-emerald-500/20 px-3 py-0.5 rounded-full border border-emerald-500/30">
                  Score: {session.previous_evaluation.score} / 10
                </span>
              </div>

              <div className="space-y-1 text-xs text-slate-300">
                <p><strong className="text-emerald-400">Strengths:</strong> {session.previous_evaluation.strengths.join(' ')}</p>
                <p><strong className="text-amber-400">Areas to Improve:</strong> {session.previous_evaluation.weaknesses.join(' ')}</p>
              </div>

              <div className="p-3 rounded-xl bg-white/5 border border-white/10 text-xs text-slate-300">
                <strong className="text-indigo-300 block mb-1">Recommended Improved Answer Sample:</strong>
                <p className="italic">{session.previous_evaluation.improved_answer_sample}</p>
              </div>
            </div>
          )}

          {/* Answer Input Area or Final Summary */}
          {!session.is_finished ? (
            <div className="glass-panel p-4 rounded-3xl border border-white/15 space-y-3">
              <textarea
                rows={5}
                value={userAnswer}
                onChange={(e) => setUserAnswer(e.target.value)}
                placeholder="Type your structured technical answer here..."
                className="glass-input w-full p-3 rounded-xl text-sm bg-slate-900 text-white resize-none font-sans"
              />
              <div className="flex justify-end">
                <button
                  onClick={handleAnswerSubmit}
                  disabled={!userAnswer.trim() || loading}
                  className="gradient-btn px-6 py-2.5 rounded-xl text-xs font-bold text-white flex items-center space-x-2 disabled:opacity-50"
                >
                  <span>Submit Answer for Evaluation</span>
                  <Send className="w-4 h-4" />
                </button>
              </div>
            </div>
          ) : (
            <div className="glass-panel p-8 rounded-3xl border border-emerald-500/30 text-center space-y-4">
              <Award className="w-16 h-16 text-emerald-400 mx-auto" />
              <h2 className="text-2xl font-extrabold text-white">Interview Complete!</h2>
              <p className="text-slate-300 text-sm">
                Overall Session Score: <strong className="text-emerald-400 text-lg">{session.final_summary?.overall_score || 8.0} / 10</strong>
              </p>
              <button
                onClick={startNewInterview}
                className="gradient-btn px-6 py-3 rounded-xl text-xs font-bold text-white uppercase tracking-wider"
              >
                Start New Practice Session
              </button>
            </div>
          )}
        </div>
      ) : (
        <div className="glass-panel p-12 rounded-3xl text-center space-y-4 border border-white/10">
          <Video className="w-12 h-12 text-indigo-400 mx-auto" />
          <h2 className="text-xl font-bold text-white">Ready for your Mock Interview?</h2>
          <p className="text-slate-400 text-sm max-w-md mx-auto">
            Select your interview category above and click "Start Mock Session" to test your knowledge step by step.
          </p>
          <button
            onClick={startNewInterview}
            className="gradient-btn px-6 py-3 rounded-xl text-xs font-bold text-white uppercase tracking-wider"
          >
            Start Mock Interview Now
          </button>
        </div>
      )}
    </div>
  );
};
