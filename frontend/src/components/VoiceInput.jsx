import React from 'react';
import { Mic, Square, Loader2 } from 'lucide-react';
import { STATUS, MESSAGES } from '../utils/constants';

const VoiceInput = ({ status, onStartListening, onStopListening }) => {
  const isListening = status === STATUS.LISTENING;
  const isProcessing = status === STATUS.PROCESSING;
  const isSpeaking = status === STATUS.SPEAKING;
  const isActive = isListening || isProcessing || isSpeaking;

  const handleClick = () => {
    if (isListening) {
      onStopListening();
    } else if (!isActive) {
      onStartListening();
    }
  };

  const getStatusMessage = () => {
    switch (status) {
      case STATUS.LISTENING:
        return MESSAGES.LISTENING;
      case STATUS.PROCESSING:
        return MESSAGES.PROCESSING;
      case STATUS.SPEAKING:
        return MESSAGES.SPEAKING;
      default:
        return MESSAGES.READY;
    }
  };

  const getButtonColor = () => {
    if (isListening) return 'bg-red-500 hover:bg-red-600';
    if (isProcessing || isSpeaking) return 'bg-pakistan-lightgreen';
    return 'bg-pakistan-green hover:bg-pakistan-lightgreen';
  };

  return (
    <div className="flex flex-col items-center space-y-6 py-8">
      {/* Voice Visualizer */}
      {isListening && (
        <div className="flex items-center justify-center space-x-2 h-16">
          {[...Array(5)].map((_, i) => (
            <div
              key={i}
              className="w-2 bg-pakistan-green rounded-full animate-wave"
              style={{
                height: '20px',
                animationDelay: `${i * 0.1}s`,
              }}
            />
          ))}
        </div>
      )}

      {/* Microphone Button */}
      <button
        onClick={handleClick}
        disabled={isProcessing || isSpeaking}
        className={`
          ${getButtonColor()}
          ${isListening ? 'pulse-ring' : ''}
          relative w-32 h-32 rounded-full
          flex items-center justify-center
          text-white shadow-2xl
          transform transition-all duration-300
          hover:scale-110
          disabled:opacity-50 disabled:cursor-not-allowed
          focus:outline-none focus:ring-4 focus:ring-pakistan-lightgreen
        `}
      >
        {isProcessing || isSpeaking ? (
          <Loader2 className="w-16 h-16 animate-spin" />
        ) : isListening ? (
          <Square className="w-16 h-16" />
        ) : (
          <Mic className="w-16 h-16" />
        )}
      </button>

      {/* Status Text */}
      <div className="text-center">
        <p className="text-2xl font-bold text-pakistan-green urdu-text">
          {getStatusMessage()}
        </p>
        <p className="text-sm text-gray-600 mt-2">
          {isListening ? 'Click to stop' : 'Click mic to speak'}
        </p>
      </div>
    </div>
  );
};

export default VoiceInput;
