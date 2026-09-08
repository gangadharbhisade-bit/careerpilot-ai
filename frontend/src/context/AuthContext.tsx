import React, { createContext, useContext, useState, useEffect } from 'react';
import { apiService } from '../services/api';

interface AuthContextType {
  user: any;
  token: string | null;
  isAuthenticated: boolean;
  login: (credentials: any) => Promise<void>;
  register: (data: any) => Promise<void>;
  guestLogin: () => Promise<void>;
  logout: () => void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<any>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('cp_auth_token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function initAuth() {
      const storedToken = localStorage.getItem('cp_auth_token');
      if (storedToken) {
        try {
          const userData = await apiService.getMe();
          setUser(userData);
        } catch (err) {
          // Token is invalid/expired
          localStorage.removeItem('cp_auth_token');
          setToken(null);
          setUser(null);
        }
      } else {
        setUser(null);
      }
      setLoading(false);
    }
    initAuth();
  }, [token]);

  const login = async (credentials: any) => {
    const res = await apiService.login(credentials);
    localStorage.setItem('cp_auth_token', res.access_token);
    setToken(res.access_token);
    setUser(res.user);
  };

  const register = async (data: any) => {
    const res = await apiService.register(data);
    localStorage.setItem('cp_auth_token', res.access_token);
    setToken(res.access_token);
    setUser(res.user);
  };

  const guestLogin = async () => {
    const res = await apiService.guestLogin();
    localStorage.setItem('cp_auth_token', res.access_token);
    setToken(res.access_token);
    setUser(res.user);
  };

  const logout = () => {
    apiService.logout().catch(() => {});
    localStorage.removeItem('cp_auth_token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        isAuthenticated: !!user,
        login,
        register,
        guestLogin,
        logout,
        loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};
