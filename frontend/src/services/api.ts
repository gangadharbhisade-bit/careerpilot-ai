const API_BASE = '/api';

export async function fetchWithAuth(endpoint: string, options: RequestInit = {}) {
  const token = localStorage.getItem('cp_auth_token');
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> || {}),
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ detail: 'Network response was not ok' }));
      throw new Error(errorData.detail || 'API request failed');
    }

    return await response.json();
  } catch (error: any) {
    console.warn(`API Error [${endpoint}]:`, error.message);
    throw error;
  }
}

export const apiService = {
  // Auth
  register: (data: any) => fetchWithAuth('/auth/register', { method: 'POST', body: JSON.stringify(data) }),
  login: (data: any) => fetchWithAuth('/auth/login', { method: 'POST', body: JSON.stringify(data) }),
  guestLogin: () => fetchWithAuth('/auth/guest', { method: 'POST' }),
  logout: () => fetchWithAuth('/auth/logout', { method: 'POST' }),
  getMe: () => fetchWithAuth('/auth/me'),

  // Profile
  getProfile: () => fetchWithAuth('/profile'),
  updateProfile: (data: any) => fetchWithAuth('/profile', { method: 'PUT', body: JSON.stringify(data) }),

  // Chat
  sendMessage: (message: string, sessionId?: number) =>
    fetchWithAuth('/chat', { method: 'POST', body: JSON.stringify({ message, session_id: sessionId }) }),
  getChatHistory: () => fetchWithAuth('/chat/history'),
  clearChatHistory: () => fetchWithAuth('/chat/clear', { method: 'DELETE' }),

  // Roadmap
  generateRoadmap: (target_career: string, duration: string, level: string) =>
    fetchWithAuth('/roadmap/generate', { method: 'POST', body: JSON.stringify({ target_career, duration, level }) }),

  // Skill Gap
  analyzeSkillGap: (current_skills: string[], target_role: string) =>
    fetchWithAuth('/skill-gap/analyze', { method: 'POST', body: JSON.stringify({ current_skills, target_role }) }),

  // Resources
  getResources: () => fetchWithAuth('/resources'),

  // Jobs & Companies
  getJobs: () => fetchWithAuth('/jobs'),
  getTargetCompanies: (career: string) => fetchWithAuth(`/companies/target?career=${encodeURIComponent(career)}`),

  // Resume
  analyzeResume: (target_role: string, resume_text: string) =>
    fetchWithAuth('/resume/analyze', { method: 'POST', body: JSON.stringify({ target_role, resume_text }) }),

  // Mock Interview
  startInterview: (target_role: string, interview_type: string) =>
    fetchWithAuth('/interview/start', { method: 'POST', body: JSON.stringify({ target_role, interview_type }) }),
  submitInterviewAnswer: (session_id: number, user_answer: string) =>
    fetchWithAuth('/interview/answer', { method: 'POST', body: JSON.stringify({ session_id, user_answer }) }),

  // Comparison
  compareCareers: (career_a: string, career_b: string) =>
    fetchWithAuth('/comparison/compare', { method: 'POST', body: JSON.stringify({ career_a, career_b }) }),

  // Progress
  getProgress: () => fetchWithAuth('/progress'),
  toggleTask: (task_id: number, completed: boolean) =>
    fetchWithAuth('/progress/task/toggle', { method: 'POST', body: JSON.stringify({ task_id, completed }) }),
  createTask: (data: any) => fetchWithAuth('/progress/task/create', { method: 'POST', body: JSON.stringify(data) }),
};
