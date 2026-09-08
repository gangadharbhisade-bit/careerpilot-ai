import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ProfileProvider } from './context/ProfileContext';
import { Sidebar } from './components/common/Sidebar';
import { Header } from './components/common/Header';
import { ScamAlertModal } from './components/common/ScamAlertModal';

// Pages
import { LandingPage } from './pages/LandingPage';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { DashboardPage } from './pages/DashboardPage';
import { ChatWindow } from './components/chat/ChatWindow';
import { RoadmapPage } from './pages/RoadmapPage';
import { SkillGapPage } from './pages/SkillGapPage';
import { ResourcesPage } from './pages/ResourcesPage';
import { JobsPage } from './pages/JobsPage';
import { CompanyPage } from './pages/CompanyPage';
import { ResumePage } from './pages/ResumePage';
import { InterviewPage } from './pages/InterviewPage';
import { ComparePage } from './pages/ComparePage';
import { PlannerPage } from './pages/PlannerPage';
import { ProfilePage } from './pages/ProfilePage';

const AppLayout: React.FC = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [scamModalOpen, setScamModalOpen] = useState(false);

  return (
    <div className="min-h-screen bg-[#0a0d14] text-slate-100 flex flex-col lg:flex-row">
      <Sidebar
        isOpen={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
        onOpenScamAlert={() => setScamModalOpen(true)}
      />

      <div className="flex-1 flex flex-col lg:pl-64 min-h-screen">
        <Header
          onToggleSidebar={() => setSidebarOpen(!sidebarOpen)}
          onOpenScamAlert={() => setScamModalOpen(true)}
        />

        <main className="flex-1">
          <Outlet />
        </main>
      </div>

      <ScamAlertModal isOpen={scamModalOpen} onClose={() => setScamModalOpen(false)} />
    </div>
  );
};

export default function App() {
  return (
    <AuthProvider>
      <ProfileProvider>
        <Router>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />

            {/* App Protected / Guided Shell */}
            <Route path="/app" element={<AppLayout />}>
              <Route index element={<Navigate to="/app/dashboard" replace />} />
              <Route path="dashboard" element={<DashboardPage />} />
              <Route path="chat" element={<ChatWindow />} />
              <Route path="roadmaps" element={<RoadmapPage />} />
              <Route path="skill-gap" element={<SkillGapPage />} />
              <Route path="resources" element={<ResourcesPage />} />
              <Route path="jobs" element={<JobsPage />} />
              <Route path="companies" element={<CompanyPage />} />
              <Route path="resume" element={<ResumePage />} />
              <Route path="interview" element={<InterviewPage />} />
              <Route path="compare" element={<ComparePage />} />
              <Route path="planner" element={<PlannerPage />} />
              <Route path="profile" element={<ProfilePage />} />
            </Route>

            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Router>
      </ProfileProvider>
    </AuthProvider>
  );
}
