import { VOICE_CONFIG, MESSAGES } from '../utils/constants';

class SpeechService {
  constructor() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    
    if (!SpeechRecognition) {
      this.recognition = null;
      return;
    }

    this.recognition = new SpeechRecognition();
    this.recognition.lang = VOICE_CONFIG.LANG_URDU;
    this.recognition.continuous = VOICE_CONFIG.CONTINUOUS;
    this.recognition.interimResults = VOICE_CONFIG.INTERIM_RESULTS;
    this.isListening = false;
    this._setupEventListeners();
  }

  _setupEventListeners() {
    if (!this.recognition) return;

    this.recognition.onresult = (event) => {
      const result = event.results[0][0];
      const transcript = result.transcript;
      console.log('🎤 Speech recognized:', transcript);
      if (this.onResultCallback) {
        this.onResultCallback(transcript, result.confidence);
      }
    };

    this.recognition.onerror = (event) => {
      console.error('Speech error:', event.error);
      this.isListening = false;
      let errorMessage = MESSAGES.ERROR;
      if (event.error === 'no-speech') errorMessage = MESSAGES.NO_SPEECH;
      if (event.error === 'not-allowed') errorMessage = MESSAGES.MIC_ERROR;
      if (this.onErrorCallback) {
        this.onErrorCallback(errorMessage, event.error);
      }
    };

    this.recognition.onend = () => {
      this.isListening = false;
      if (this.onEndCallback) this.onEndCallback();
    };

    this.recognition.onstart = () => {
      this.isListening = true;
    };
  }

  startListening(onResult, onError, onEnd) {
    if (!this.recognition) {
      if (onError) onError('Speech not supported', 'not-supported');
      return;
    }
    if (this.isListening) return;

    this.onResultCallback = onResult;
    this.onErrorCallback = onError;
    this.onEndCallback = onEnd;

    try {
      this.recognition.start();
    } catch (error) {
      if (onError) onError(MESSAGES.ERROR, error.message);
    }
  }

  stopListening() {
    if (this.recognition && this.isListening) {
      this.recognition.stop();
    }
  }

  isSupported() {
    return this.recognition !== null;
  }
}

export default new SpeechService();
