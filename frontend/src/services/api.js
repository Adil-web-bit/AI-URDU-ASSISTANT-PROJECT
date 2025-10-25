import axios from 'axios';
import { API_BASE_URL, API_ENDPOINTS } from '../utils/constants';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
});

apiClient.interceptors.request.use(
  (config) => {
    console.log('🚀 API Request:', config.method.toUpperCase(), config.url);
    return config;
  },
  (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(
  (response) => {
    console.log('✅ API Response:', response.status);
    return response;
  },
  (error) => {
    console.error('❌ Response Error:', error.message);
    return Promise.reject(error);
  }
);

const api = {
  processCommand: async (text, language = 'auto') => {
    const response = await apiClient.post(API_ENDPOINTS.PROCESS_COMMAND, {
      text,
      language,
      user_id: 'web_user_' + Date.now()
    });
    return response.data;
  },

  getAudioUrl: (filename) => {
    if (!filename) return null;
    return `${API_BASE_URL}${API_ENDPOINTS.GET_AUDIO}/${filename}`;
  },

  getCommands: async () => {
    const response = await apiClient.get(API_ENDPOINTS.GET_COMMANDS);
    return response.data;
  },

  healthCheck: async () => {
    const response = await apiClient.get(API_ENDPOINTS.HEALTH);
    return response.data;
  }
};

export default api;
