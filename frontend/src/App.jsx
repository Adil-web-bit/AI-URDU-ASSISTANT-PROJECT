import React, { useState, useCallback, useEffect } from 'react';
import Header from './components/Header';
import VoiceInput from './components/VoiceInput';
import ChatWindow from './components/ChatWindow';
import QuickCommands from './components/QuickCommands';
import Footer from './components/Footer';
import api from './services/api';
import audioService from './services/audioService';
import speechService from './services/speechService';
import { STATUS, MESSAGE_TYPE, MESSAGES } from './utils/constants';
import { AlertCircle, Wifi, WifiOff } from 'lucide-react';

function App() {
  const [status, setStatus] = useState(STATUS.IDLE);
  const [messages, setMessages] = useState([]);
  const [error, setError] = useState(null);
  const [isBackendConnected, setIsBackendConnected] = useState(false);

  // Check backend connection on mount
  useEffect(() => {
    checkBackendConnection();
  }, []);

  const checkBackendConnection = async () => {
    try {
      await api.healthCheck();
      setIsBackendConnected(true);
      console.log('✅ Backend connected');
    } catch (error) {
      setIsBackendConnected(false);
      console.error('❌ Backend not connected');
    }
  };

  // Add user message to chat
  const addUserMessage = useCallback((text) => {
    const message = {
      id: Date.now(),
      type: MESSAGE_TYPE.USER,
      text: text,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, message]);
    return message;
  }, []);

  // Add assistant message to chat
  const addAssistantMessage = useCallback((text) => {
    const message = {
      id: Date.now() + 1,
      type: MESSAGE_TYPE.ASSISTANT,
      text: text,
      timestamp: new Date().toISOString()
    };
    setMessages(prev => [...prev, message]);
    return message;
  }, []);

  // Process command and get response
  const processCommand = useCallback(async (text) => {
    try {
      setStatus(STATUS.PROCESSING);
      setError(null);

      console.log('📤 Processing command:', text);

      // Add user message
      addUserMessage(text);

      // Call API
      const response = await api.processCommand(text);
      console.log('📥 API Response:', response);

      // Add assistant response
      addAssistantMessage(response.response_text);

      // Play audio if available
      if (response.audio_file) {
        setStatus(STATUS.SPEAKING);
        const audioUrl = api.getAudioUrl(response.audio_file);
        console.log('🔊 Playing audio:', audioUrl);
        
        await audioService.play(
          audioUrl,
          () => {
            // On audio end
            console.log('✅ Audio playback finished');
            setStatus(STATUS.IDLE);
          },
          (error) => {
            // On audio error
            console.error('❌ Audio playback error:', error);
            setStatus(STATUS.IDLE);
            setError('Audio playback failed');
          }
        );
      } else {
        setStatus(STATUS.IDLE);
      }

    } catch (error) {
      console.error('❌ Command processing failed:', error);
      setStatus(STATUS.IDLE);
      
      let errorMessage = 'کچھ غلطی ہو گئی';
      if (error.response) {
        errorMessage = `Server error: ${error.response.status}`;
      } else if (error.request) {
        errorMessage = 'بیک اینڈ سے رابطہ نہیں ہو سکا';
      }
      
      setError(errorMessage);
      addAssistantMessage(errorMessage);
    }
  }, [addUserMessage, addAssistantMessage]);

  // Handle voice recognition result
  const handleVoiceResult = useCallback((transcript, confidence) => {
    console.log('🎤 Voice result:', transcript, `(${(confidence * 100).toFixed(0)}%)`);
    processCommand(transcript);
  }, [processCommand]);

  // Handle voice recognition error
  const handleVoiceError = useCallback((message, errorType) => {
    console.error('🎤 Voice error:', errorType, message);
    setStatus(STATUS.IDLE);
    setError(message);
    
    // Add error message to chat
    addAssistantMessage(message);
  }, [addAssistantMessage]);

  // Handle voice recognition end
  const handleVoiceEnd = useCallback(() => {
    console.log('🎤 Voice recognition ended');
    if (status === STATUS.LISTENING) {
      setStatus(STATUS.IDLE);
    }
  }, [status]);

  // Start listening for voice input
  const handleStartListening = useCallback(() => {
    if (!speechService.isSupported()) {
      setError('آپ کا براؤزر وائس ریکگنیشن سپورٹ نہیں کرتا');
      return;
    }

    setStatus(STATUS.LISTENING);
    setError(null);
    
    speechService.startListening(
      handleVoiceResult,
      handleVoiceError,
      handleVoiceEnd
    );
  }, [handleVoiceResult, handleVoiceError, handleVoiceEnd]);

  // Stop listening
  const handleStopListening = useCallback(() => {
    speechService.stopListening();
    setStatus(STATUS.IDLE);
  }, []);

  // Handle quick command click
  const handleQuickCommand = useCallback((command) => {
    console.log('Quick command:', command);
    processCommand(command);
  }, [processCommand]);

  // Check if any action is in progress
  const isActionInProgress = status !== STATUS.IDLE;

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 to-pakistan-cream">
      {/* Header */}
      <Header />

      {/* Main Content */}
      <main className="flex-grow container mx-auto px-4 py-8 max-w-4xl">
        
        {/* Backend Connection Status */}
        <div className="mb-4">
          {isBackendConnected ? (
            <div className="flex items-center justify-center space-x-2 text-green-600 text-sm">
              <Wifi className="w-4 h-4" />
              <span>Backend Connected</span>
            </div>
          ) : (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
              <div className="flex items-center space-x-2 text-red-600">
                <WifiOff className="w-5 h-5" />
                <span className="font-medium">Backend not connected</span>
              </div>
              <p className="text-sm text-red-500 mt-1">
                Make sure backend is running at http://localhost:8000
              </p>
              <button
                onClick={checkBackendConnection}
                className="mt-2 text-sm text-red-600 underline hover:text-red-700"
              >
                Retry Connection
              </button>
            </div>
          )}
        </div>

        {/* Error Display */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6 flex items-start space-x-3">
            <AlertCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
            <div>
              <p className="text-red-700 font-medium">خرابی</p>
              <p className="text-red-600 text-sm mt-1">{error}</p>
            </div>
          </div>
        )}

        {/* Welcome Message */}
        {messages.length === 0 && (
          <div className="bg-white rounded-lg shadow-lg p-8 mb-6 text-center">
            <h2 className="text-3xl font-bold text-pakistan-green mb-4 urdu-text">
              خوش آمدید!
            </h2>
            <p className="text-gray-600 mb-6">
              Welcome to Urdu Voice Assistant. Click the microphone and start speaking in Urdu or English.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
              <div className="bg-pakistan-cream p-4 rounded-lg">
                <h3 className="font-bold text-pakistan-green mb-2">🎤 Step 1</h3>
                <p className="text-sm text-gray-700">Click the microphone button</p>
              </div>
              <div className="bg-pakistan-cream p-4 rounded-lg">
                <h3 className="font-bold text-pakistan-green mb-2">🗣️ Step 2</h3>
                <p className="text-sm text-gray-700">Speak your command in Urdu/English</p>
              </div>
              <div className="bg-pakistan-cream p-4 rounded-lg">
                <h3 className="font-bold text-pakistan-green mb-2">🔊 Step 3</h3>
                <p className="text-sm text-gray-700">Listen to the response</p>
              </div>
            </div>
          </div>
        )}

        {/* Chat Window */}
        {messages.length > 0 && (
          <ChatWindow messages={messages} />
        )}

        {/* Voice Input */}
        <div className="bg-white rounded-lg shadow-lg mb-6">
          <VoiceInput
            status={status}
            onStartListening={handleStartListening}
            onStopListening={handleStopListening}
          />
        </div>

        {/* Quick Commands */}
        <QuickCommands
          onCommandClick={handleQuickCommand}
          disabled={isActionInProgress}
        />

        {/* Features Section */}
        <div className="mt-8 bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold text-pakistan-green mb-4">
            خصوصیات
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="flex items-start space-x-3">
              <div className="bg-pakistan-green text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0">
                ✓
              </div>
              <div>
                <h4 className="font-semibold text-gray-800">Urdu Voice Recognition</h4>
                <p className="text-sm text-gray-600">Understands Urdu and English commands</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="bg-pakistan-green text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0">
                ✓
              </div>
              <div>
                <h4 className="font-semibold text-gray-800">Natural Urdu Responses</h4>
                <p className="text-sm text-gray-600">Speaks back in natural Urdu voice</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="bg-pakistan-green text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0">
                ✓
              </div>
              <div>
                <h4 className="font-semibold text-gray-800">Multiple Commands</h4>
                <p className="text-sm text-gray-600">Weather, time, prayers, jokes, and more</p>
              </div>
            </div>
            <div className="flex items-start space-x-3">
              <div className="bg-pakistan-green text-white rounded-full w-8 h-8 flex items-center justify-center flex-shrink-0">
                ✓
              </div>
              <div>
                <h4 className="font-semibold text-gray-800">100% Free</h4>
                <p className="text-sm text-gray-600">No API keys or paid services required</p>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default App;
