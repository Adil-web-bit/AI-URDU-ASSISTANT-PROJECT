import React from 'react';
import { User, Bot } from 'lucide-react';
import { MESSAGE_TYPE } from '../utils/constants';

const MessageBubble = ({ message }) => {
  const isUser = message.type === MESSAGE_TYPE.USER;

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} fade-in`}>
      <div className={`flex items-start space-x-3 max-w-md ${isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
        {/* Avatar */}
        <div className={`
          flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center
          ${isUser ? 'bg-blue-500' : 'bg-pakistan-green'}
        `}>
          {isUser ? (
            <User className="w-6 h-6 text-white" />
          ) : (
            <Bot className="w-6 h-6 text-white" />
          )}
        </div>

        {/* Message Content */}
        <div className={`
          px-4 py-3 rounded-2xl shadow-md
          ${isUser 
            ? 'bg-blue-500 text-white rounded-tr-none' 
            : 'bg-gray-100 text-gray-800 rounded-tl-none'
          }
        `}>
          <p className={`text-base urdu-text ${isUser ? 'text-right' : 'text-left'}`}>
            {message.text}
          </p>
          {message.timestamp && (
            <p className={`text-xs opacity-70 mt-1 ${isUser ? 'text-right' : 'text-left'}`}>
              {new Date(message.timestamp).toLocaleTimeString('ur-PK', {
                hour: '2-digit',
                minute: '2-digit'
              })}
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default MessageBubble;
