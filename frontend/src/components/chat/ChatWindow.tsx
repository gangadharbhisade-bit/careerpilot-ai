import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Send, Bot, User, Sparkles, Mic, MicOff, Copy, Check, BookOpen, ExternalLink, RefreshCw, Briefcase, Code, Compass, Map, Scale, CheckCircle2, Zap } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { apiService } from '../../services/api';
import { ChatMessage } from '../../types';

const PRESET_PROMPTS = [
  "Python free me kaise sikhe?",
  "Data Analyst vs Data Scientist",
  "Android Developer kaise bane?",
  "Cybersecurity me career kaise start karu?",
  "Frontend Developer ke liye projects batao",
  "Python me next kya sikhu?"
];

export const ChatWindow: React.FC = () => {
  const navigate = useNavigate();
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      sender: 'assistant',
      content: `👋 **Welcome to CareerPilot AI!**

I am your general-purpose AI Career Counselor. Ask me anything about career guidance, skill progression, learning resources, resume reviews, target companies, job applications, or interview preparation.

Try asking: *"Python free me kaise sikhe?"*, *"Data Analyst vs Data Scientist"*, or *"Android Developer kaise bane?"*`,
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);
  const [isListening, setIsListening] = useState(false);
  const [isDemoMode, setIsDemoMode] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSend = async (textToSend?: string) => {
    const query = textToSend || input;
    if (!query.trim() || loading) return;

    const userMsg: ChatMessage = { sender: 'user', content: query };
    setMessages((prev) => [...prev, userMsg]);
    if (!textToSend) setInput('');
    setLoading(true);

    try {
      const res = await apiService.sendMessage(query);
      setIsDemoMode(res.is_demo_mode ?? true);
      const assistantMsg: ChatMessage = {
        sender: 'assistant',
        content: res.reply,
        structured_payload: res.structured_payload,
      };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err: any) {
      setMessages((prev) => [
        ...prev,
        {
          sender: 'assistant',
          content: '⚠️ Something went wrong generating your career response. Please try again.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = (text: string, index: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const toggleVoice = () => {
    setIsListening(!isListening);
    if (!isListening) {
      setInput('Python free me kaise sikhe?');
    }
  };

  return (
    <div className="flex flex-col h-[calc(100vh-80px)] max-w-5xl mx-auto p-3 sm:p-6">
      {/* Header Banner */}
      <div className="glass-panel p-4 rounded-2xl mb-4 flex items-center justify-between border border-indigo-500/20 shadow-lg">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center text-white shadow-md">
            <Bot className="w-6 h-6" />
          </div>
          <div>
            <h2 className="font-bold text-white text-base flex items-center gap-2">
              CareerPilot AI Counselor
              <span
                className={`text-[10px] font-extrabold px-2 py-0.5 rounded-full border ${
                  isDemoMode
                    ? 'bg-amber-500/20 text-amber-300 border-amber-500/30'
                    : 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30'
                }`}
              >
                {isDemoMode ? 'Demo Counselor Mode' : 'Live AI Mode'}
              </span>
            </h2>
            <p className="text-xs text-indigo-300">Multi-Intent Guidance • Free Resources • Comparisons • Roadmaps</p>
          </div>
        </div>
        <button
          onClick={() => setMessages([messages[0]])}
          className="p-2 rounded-xl bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white transition text-xs flex items-center space-x-1"
          title="Clear Chat History"
        >
          <RefreshCw className="w-4 h-4" />
          <span className="hidden sm:inline">Reset</span>
        </button>
      </div>

      {/* Messages Scroll Area */}
      <div className="flex-1 overflow-y-auto space-y-4 pr-2 mb-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex items-start space-x-3 ${
              msg.sender === 'user' ? 'flex-row-reverse space-x-reverse' : ''
            }`}
          >
            {/* Avatar */}
            <div
              className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 text-white font-bold text-xs shadow-md ${
                msg.sender === 'user'
                  ? 'bg-gradient-to-tr from-indigo-500 to-cyan-500'
                  : 'bg-gradient-to-tr from-purple-600 to-indigo-600'
              }`}
            >
              {msg.sender === 'user' ? <User className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
            </div>

            {/* Bubble */}
            <div
              className={`max-w-[90%] sm:max-w-[85%] p-4 rounded-2xl text-sm leading-relaxed relative group shadow-md ${
                msg.sender === 'user'
                  ? 'bg-indigo-600/90 text-white rounded-tr-none'
                  : 'glass-panel text-slate-200 rounded-tl-none border border-white/10'
              }`}
            >
              {msg.sender === 'assistant' && (
                <button
                  onClick={() => handleCopy(msg.content, idx)}
                  className="absolute top-3 right-3 opacity-0 group-hover:opacity-100 p-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-slate-300 transition"
                  title="Copy Response"
                >
                  {copiedIndex === idx ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              )}

              {/* Enhanced ReactMarkdown Renderer */}
              <div className="prose prose-invert prose-sm max-w-none">
                <ReactMarkdown
                  remarkPlugins={[remarkGfm]}
                  components={{
                    table: ({ node, ...props }) => (
                      <div className="overflow-x-auto my-3 rounded-xl border border-indigo-500/30 glass-panel shadow-md">
                        <table className="w-full text-left border-collapse" {...props} />
                      </div>
                    ),
                    thead: ({ node, ...props }) => (
                      <thead className="bg-indigo-950/80 text-indigo-200 border-b border-indigo-500/30" {...props} />
                    ),
                    th: ({ node, ...props }) => (
                      <th className="px-3.5 py-2.5 text-xs font-extrabold uppercase tracking-wider text-indigo-300" {...props} />
                    ),
                    td: ({ node, ...props }) => (
                      <td className="px-3.5 py-2 text-xs border-b border-white/5 text-slate-200" {...props} />
                    ),
                    a: ({ node, ...props }) => (
                      <a className="text-indigo-400 font-semibold hover:underline" target="_blank" rel="noreferrer" {...props} />
                    ),
                    code: ({ node, inline, ...props }: any) =>
                      inline ? (
                        <code className="bg-white/10 text-indigo-300 px-1.5 py-0.5 rounded text-xs font-mono" {...props} />
                      ) : (
                        <code className="block bg-slate-900/90 text-indigo-200 p-3 rounded-xl text-xs overflow-x-auto my-2 border border-white/10 font-mono" {...props} />
                      )
                  }}
                >
                  {msg.content}
                </ReactMarkdown>
              </div>

              {/* RENDER STRUCTURED SIDE-BY-SIDE CAREER COMPARISON UI */}
              {msg.structured_payload?.comparison_data && (
                <div className="mt-5 pt-4 border-t border-indigo-500/30 space-y-4">
                  <div className="flex items-center space-x-2 text-indigo-300 text-xs font-bold uppercase tracking-wider">
                    <Scale className="w-4 h-4 text-indigo-400" />
                    <span>{msg.structured_payload.comparison_data.title}</span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {/* Card A */}
                    {msg.structured_payload.comparison_data.career_a && (
                      <div className="glass-panel p-4 rounded-2xl border border-indigo-500/30 bg-indigo-950/20 space-y-3">
                        <h4 className="text-base font-extrabold text-indigo-300 flex items-center gap-1.5">
                          <span>📊 {msg.structured_payload.comparison_data.career_a.name}</span>
                        </h4>

                        <div className="text-xs text-slate-300 space-y-2">
                          <p><strong className="text-white">Primary Focus:</strong> {msg.structured_payload.comparison_data.career_a.focus}</p>
                          <div>
                            <strong className="text-white block mb-1">Key Skills:</strong>
                            <div className="flex flex-wrap gap-1">
                              {msg.structured_payload.comparison_data.career_a.key_skills?.map((sk: string, sI: number) => (
                                <span key={sI} className="bg-indigo-500/20 text-indigo-200 text-[11px] px-2 py-0.5 rounded-md border border-indigo-500/30">
                                  {sk}
                                </span>
                              ))}
                            </div>
                          </div>
                          <p><strong className="text-white">Coding Depth:</strong> <span className="text-amber-300 font-semibold">{msg.structured_payload.comparison_data.career_a.coding_level}</span></p>
                          <p><strong className="text-white">Math Requirement:</strong> <span className="text-purple-300 font-semibold">{msg.structured_payload.comparison_data.career_a.math_level}</span></p>
                          <p><strong className="text-white">Learning Curve:</strong> <span className="text-emerald-300 font-semibold">{msg.structured_payload.comparison_data.career_a.learning_curve}</span></p>
                        </div>
                      </div>
                    )}

                    {/* Card B */}
                    {msg.structured_payload.comparison_data.career_b && (
                      <div className="glass-panel p-4 rounded-2xl border border-purple-500/30 bg-purple-950/20 space-y-3">
                        <h4 className="text-base font-extrabold text-purple-300 flex items-center gap-1.5">
                          <span>🤖 {msg.structured_payload.comparison_data.career_b.name}</span>
                        </h4>

                        <div className="text-xs text-slate-300 space-y-2">
                          <p><strong className="text-white">Primary Focus:</strong> {msg.structured_payload.comparison_data.career_b.focus}</p>
                          <div>
                            <strong className="text-white block mb-1">Key Skills:</strong>
                            <div className="flex flex-wrap gap-1">
                              {msg.structured_payload.comparison_data.career_b.key_skills?.map((sk: string, sI: number) => (
                                <span key={sI} className="bg-purple-500/20 text-purple-200 text-[11px] px-2 py-0.5 rounded-md border border-purple-500/30">
                                  {sk}
                                </span>
                              ))}
                            </div>
                          </div>
                          <p><strong className="text-white">Coding Depth:</strong> <span className="text-amber-300 font-semibold">{msg.structured_payload.comparison_data.career_b.coding_level}</span></p>
                          <p><strong className="text-white">Math Requirement:</strong> <span className="text-purple-300 font-semibold">{msg.structured_payload.comparison_data.career_b.math_level}</span></p>
                          <p><strong className="text-white">Learning Curve:</strong> <span className="text-emerald-300 font-semibold">{msg.structured_payload.comparison_data.career_b.learning_curve}</span></p>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Recommendation Verdict Banner */}
                  {msg.structured_payload.comparison_data.recommendation && (
                    <div className="p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-xs text-emerald-200 flex items-start space-x-2">
                      <Zap className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                      <div>
                        <strong className="text-emerald-300 block font-bold mb-0.5">Counselor Recommendation:</strong>
                        <span>{msg.structured_payload.comparison_data.recommendation}</span>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Action Button to Open Full Interactive Roadmap */}
              {msg.structured_payload?.target_role && msg.structured_payload?.intent === 'ROADMAP' && (
                <div className="mt-4 pt-3 border-t border-white/10">
                  <button
                    onClick={() => navigate(`/app/roadmaps?career=${encodeURIComponent(msg.structured_payload.target_role)}`)}
                    className="gradient-btn w-full py-2.5 px-4 rounded-xl text-xs font-bold text-white flex items-center justify-center space-x-2 shadow-lg"
                  >
                    <Map className="w-4 h-4" />
                    <span>View Full Interactive {msg.structured_payload.target_role} Roadmap</span>
                  </button>
                </div>
              )}

              {/* Render Structured Interactive Resource Cards */}
              {msg.structured_payload?.resources?.free && (
                <div className="mt-4 pt-3 border-t border-white/10 space-y-2">
                  <p className="text-xs font-semibold text-indigo-300 flex items-center gap-1">
                    <BookOpen className="w-3.5 h-3.5" /> Verified Learning Resources:
                  </p>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    {msg.structured_payload.resources.free.map((res: any, rIdx: number) => (
                      <a
                        key={rIdx}
                        href={res.url}
                        target="_blank"
                        rel="noreferrer"
                        className="p-2.5 rounded-xl bg-white/5 hover:bg-indigo-600/20 border border-white/10 hover:border-indigo-500/40 flex items-center justify-between text-xs text-slate-200 hover:text-white transition"
                      >
                        <span className="truncate font-medium">{res.title}</span>
                        <div className="flex items-center space-x-1 shrink-0 ml-2">
                          <span className="text-[9px] bg-emerald-500/20 text-emerald-300 px-1.5 py-0.5 rounded font-bold">FREE</span>
                          <ExternalLink className="w-3.5 h-3.5 text-indigo-400" />
                        </div>
                      </a>
                    ))}
                  </div>
                </div>
              )}

              {msg.structured_payload?.application_channels && (
                <div className="mt-4 pt-3 border-t border-white/10 space-y-2">
                  <p className="text-xs font-semibold text-emerald-300 flex items-center gap-1">
                    <Briefcase className="w-3.5 h-3.5" /> Direct Hiring Portals:
                  </p>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                    {msg.structured_payload.application_channels.map((chan: any, cIdx: number) => (
                      <a
                        key={cIdx}
                        href={chan.url}
                        target="_blank"
                        rel="noreferrer"
                        className="p-2 rounded-lg bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-between text-xs text-emerald-200 transition"
                      >
                        <span className="font-semibold">{chan.name}</span>
                        <ExternalLink className="w-3 h-3 text-emerald-400 shrink-0 ml-2" />
                      </a>
                    ))}
                  </div>
                </div>
              )}

              {msg.structured_payload?.skills_to_learn && (
                <div className="mt-4 pt-3 border-t border-white/10 space-y-2">
                  <p className="text-xs font-semibold text-purple-300 flex items-center gap-1">
                    <Compass className="w-3.5 h-3.5" /> Next Priority Skills:
                  </p>
                  <div className="flex flex-wrap gap-1.5">
                    {msg.structured_payload.skills_to_learn.map((skill: string, sIdx: number) => (
                      <span key={sIdx} className="text-xs bg-purple-500/20 text-purple-200 border border-purple-500/30 px-2.5 py-1 rounded-full">
                        • {skill}
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded-xl bg-purple-600/50 flex items-center justify-center text-white">
              <Bot className="w-4 h-4 animate-spin" />
            </div>
            <div className="glass-panel p-3.5 rounded-2xl text-xs text-indigo-300 flex items-center space-x-2">
              <Sparkles className="w-4 h-4 animate-pulse text-indigo-400" />
              <span>Analyzing query & crafting general career guidance...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Quick Preset Prompts */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 mb-2 no-scrollbar">
        {PRESET_PROMPTS.map((prompt, idx) => (
          <button
            key={idx}
            onClick={() => handleSend(prompt)}
            className="shrink-0 text-xs bg-white/5 hover:bg-indigo-600/20 text-slate-300 hover:text-indigo-300 border border-white/10 hover:border-indigo-500/40 px-3 py-1.5 rounded-full transition whitespace-nowrap"
          >
            {prompt}
          </button>
        ))}
      </div>

      {/* Input Box */}
      <div className="glass-panel p-2 sm:p-3 rounded-2xl border border-white/15 shadow-xl flex items-center gap-2">
        <button
          onClick={toggleVoice}
          className={`p-2.5 rounded-xl transition ${
            isListening ? 'bg-rose-500 text-white animate-pulse' : 'bg-white/5 text-slate-400 hover:text-white'
          }`}
          title="Voice input simulation"
        >
          {isListening ? <MicOff className="w-5 h-5" /> : <Mic className="w-5 h-5" />}
        </button>

        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Ask anything about your career..."
          className="flex-1 bg-transparent text-white text-sm focus:outline-none px-2 placeholder-slate-500"
        />

        <button
          onClick={() => handleSend()}
          disabled={!input.trim() || loading}
          className="gradient-btn p-2.5 rounded-xl text-white disabled:opacity-40 disabled:cursor-not-allowed"
        >
          <Send className="w-5 h-5" />
        </button>
      </div>
    </div>
  );
};
