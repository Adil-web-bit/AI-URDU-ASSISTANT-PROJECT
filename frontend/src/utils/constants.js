export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const API_ENDPOINTS = {
  PROCESS_COMMAND: '/api/v1/process-command',
  GET_AUDIO: '/api/v1/audio',
  GET_COMMANDS: '/api/v1/commands',
  HEALTH: '/health',
};

export const VOICE_CONFIG = {
  LANG_URDU: 'ur-PK',
  LANG_ENGLISH: 'en-US',
  CONTINUOUS: false,
  INTERIM_RESULTS: false,
};

export const MESSAGES = {
  LISTENING: 'سن رہے ہیں...',
  PROCESSING: 'پروسیس کر رہے ہیں...',
  SPEAKING: 'بول رہے ہیں...',
  READY: 'سننے کے لیے تیار',
  ERROR: 'کچھ غلطی ہو گئی',
  NO_SPEECH: 'کچھ سنائی نہیں دیا',
  MIC_ERROR: 'مائیکروفون کی اجازت نہیں ملی',
};

export const QUICK_COMMANDS = [
  { id: 1, text: 'موسم بتائیں', icon: 'CloudSun', command: 'weather' },
  { id: 2, text: 'وقت بتائیں', icon: 'Clock', command: 'what time is it' },
  { id: 3, text: 'تاریخ بتائیں', icon: 'Calendar', command: 'what is the date' },
  { id: 4, text: 'لطیفہ سنائیں', icon: 'Laugh', command: 'tell me a joke' },
  { id: 5, text: 'ہیلو', icon: 'Hand', command: 'hello' },
  { id: 6, text: 'مدد', icon: 'HelpCircle', command: 'help' }
];

export const STATUS = {
  IDLE: 'idle',
  LISTENING: 'listening',
  PROCESSING: 'processing',
  SPEAKING: 'speaking',
  ERROR: 'error'
};

export const MESSAGE_TYPE = {
  USER: 'user',
  ASSISTANT: 'assistant'
};
