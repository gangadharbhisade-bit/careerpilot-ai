import React, { useState, useEffect } from 'react';
import { CheckSquare, Plus, Clock, Sparkles, CheckCircle2 } from 'lucide-react';
import { apiService } from '../services/api';

export const PlannerPage: React.FC = () => {
  const [plannerData, setPlannerData] = useState<any>(null);
  const [newTaskText, setNewTaskText] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchProgress = async () => {
    try {
      const data = await apiService.getProgress();
      setPlannerData(data.daily_planner);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchProgress();
  }, []);

  const handleToggle = async (taskId: number, currentCompleted: boolean) => {
    try {
      await apiService.toggleTask(taskId, !currentCompleted);
      fetchProgress();
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreateTask = async () => {
    if (!newTaskText.trim()) return;
    try {
      await apiService.createTask({
        task_text: newTaskText.trim(),
        topic: 'Custom',
        estimated_minutes: 30,
        date_str: new Date().toISOString().split('T')[0],
      });
      setNewTaskText('');
      fetchProgress();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="p-4 sm:p-8 max-w-5xl mx-auto space-y-6">
      <div className="glass-panel p-6 rounded-3xl border border-indigo-500/20 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="p-2.5 rounded-xl bg-indigo-600/20 text-indigo-400 border border-indigo-500/30">
            <CheckSquare className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-extrabold text-white">Daily Learning Planner</h1>
            <p className="text-slate-400 text-sm">
              Structured study schedules, practice tasks, and daily completion tracking.
            </p>
          </div>
        </div>

        {plannerData && (
          <div className="flex items-center space-x-2 bg-indigo-500/10 border border-indigo-500/30 px-4 py-2 rounded-2xl">
            <Sparkles className="w-4 h-4 text-indigo-400" />
            <span className="text-xs font-bold text-white">
              {plannerData.completed_tasks} / {plannerData.total_tasks} Tasks ({plannerData.completion_percentage}%)
            </span>
          </div>
        )}
      </div>

      {/* Create New Task */}
      <div className="glass-panel p-4 rounded-2xl border border-white/10 flex items-center gap-2">
        <input
          type="text"
          value={newTaskText}
          onChange={(e) => setNewTaskText(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleCreateTask()}
          placeholder="Add a new daily learning goal (e.g. Solve 2 LeetCode problems)..."
          className="glass-input flex-1 p-3 rounded-xl text-xs bg-slate-900"
        />
        <button
          onClick={handleCreateTask}
          className="gradient-btn px-4 py-3 rounded-xl text-xs font-bold text-white flex items-center space-x-1.5 shrink-0"
        >
          <Plus className="w-4 h-4" />
          <span>Add Task</span>
        </button>
      </div>

      {/* Task List */}
      {plannerData && (
        <div className="space-y-3">
          {plannerData.tasks.map((task: any) => (
            <div
              key={task.id}
              onClick={() => handleToggle(task.id, task.completed)}
              className={`p-4 rounded-2xl border transition cursor-pointer flex items-center justify-between ${
                task.completed
                  ? 'bg-emerald-950/20 border-emerald-500/30 text-slate-400'
                  : 'glass-panel border-white/10 text-white hover:border-indigo-500/40'
              }`}
            >
              <div className="flex items-center space-x-3">
                <div
                  className={`w-5 h-5 rounded-lg border flex items-center justify-center transition ${
                    task.completed
                      ? 'bg-emerald-500 border-emerald-400 text-white'
                      : 'border-slate-500 bg-white/5'
                  }`}
                >
                  {task.completed && <CheckCircle2 className="w-3.5 h-3.5" />}
                </div>
                <span className={`text-sm ${task.completed ? 'line-through text-slate-500' : 'font-medium'}`}>
                  {task.task_text}
                </span>
              </div>

              <div className="flex items-center space-x-2 shrink-0">
                <span className="text-[10px] font-semibold bg-white/5 px-2.5 py-1 rounded-full text-indigo-300">
                  {task.topic}
                </span>
                <span className="text-xs text-slate-400 flex items-center gap-1">
                  <Clock className="w-3 h-3 text-slate-500" /> {task.estimated_minutes}m
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
