export interface UserProfile {
  education: string;
  degree: string;
  branch: string;
  current_role: string;
  experience_level: string;
  skills: string[];
  programming_languages: string[];
  interests: string[];
  target_career: string;
  target_industry: string;
  preferred_location: string;
  remote_preference: string;
  salary_expectation: string;
  available_learning_time: string;
  career_goal: string;
  current_projects: string[];
  certifications: string[];
}

export interface ChatMessage {
  id?: number;
  sender: 'user' | 'assistant';
  content: string;
  structured_payload?: any;
  created_at?: string;
}

export interface WeeklyPlan {
  week: number;
  title: string;
  topics: string[];
  practice: string;
}

export interface PhasePlan {
  phase_number: number;
  phase_title: string;
  duration_weeks: number;
  skills_covered: string[];
  weekly_breakdown: WeeklyPlan[];
  milestone_project: string;
  learning_resources: { title: string; url: string; type: string; badge: string }[];
}

export interface RoadmapData {
  target_career: string;
  duration: string;
  level: string;
  overview: string;
  phases: PhasePlan[];
}

export interface SkillGapData {
  target_role: string;
  current_skills: string[];
  required_skills: string[];
  missing_skills: string[];
  readiness_percentage: number;
  priority_order: { skill: string; priority: string; hours: number; resource: string }[];
}

export interface ResumeAnalysisData {
  ats_score: number;
  matched_keywords: string[];
  missing_keywords: string[];
  strengths: string[];
  improvements: string[];
  suggested_bullet_points: { original: string; improved: string }[];
  actionable_next_steps: string[];
}

export interface QuestionEvaluation {
  score: number;
  strengths: string[];
  weaknesses: string[];
  improved_answer_sample: string;
}

export interface InterviewTurn {
  session_id: number;
  question_number: number;
  question: string;
  previous_evaluation?: QuestionEvaluation;
  is_finished: boolean;
  final_summary?: any;
}
