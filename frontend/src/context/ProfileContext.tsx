import React, { createContext, useContext, useState, useEffect } from 'react';
import { UserProfile } from '../types';
import { apiService } from '../services/api';
import { useAuth } from './AuthContext';

interface ProfileContextType {
  profile: UserProfile;
  updateProfile: (data: Partial<UserProfile>) => Promise<void>;
  refetchProfile: () => Promise<void>;
  loading: boolean;
}

const emptyProfile: UserProfile = {
  education: '',
  degree: '',
  branch: '',
  current_role: '',
  experience_level: 'Beginner',
  skills: [],
  programming_languages: [],
  interests: [],
  target_career: '',
  target_industry: 'Technology',
  preferred_location: 'Remote',
  remote_preference: 'Remote',
  salary_expectation: '',
  available_learning_time: '2 hours/day',
  career_goal: '',
  current_projects: [],
  certifications: [],
};

const ProfileContext = createContext<ProfileContextType | undefined>(undefined);

export const ProfileProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { token, user } = useAuth();
  const [profile, setProfile] = useState<UserProfile>(emptyProfile);
  const [loading, setLoading] = useState(true);

  const fetchProfileData = async () => {
    if (!token || !user) {
      setProfile(emptyProfile);
      setLoading(false);
      return;
    }
    setLoading(true);
    try {
      const data = await apiService.getProfile();
      setProfile(data);
    } catch (err) {
      console.warn('Failed to load profile for user');
      setProfile(emptyProfile);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfileData();
  }, [token, user?.id]);

  const updateProfile = async (updatedFields: Partial<UserProfile>) => {
    const updated = { ...profile, ...updatedFields };
    setProfile(updated);
    try {
      const res = await apiService.updateProfile(updated);
      setProfile(res);
    } catch (err) {
      console.warn('Profile update synced locally.');
    }
  };

  return (
    <ProfileContext.Provider value={{ profile, updateProfile, refetchProfile: fetchProfileData, loading }}>
      {children}
    </ProfileContext.Provider>
  );
};

export const useProfile = () => {
  const context = useContext(ProfileContext);
  if (!context) throw new Error('useProfile must be used within ProfileProvider');
  return context;
};
