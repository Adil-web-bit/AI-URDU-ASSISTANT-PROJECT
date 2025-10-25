import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';

const ChatWindow = ({ messages }) => {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 mb-6 max-h-96 overflow-y-auto">
      <h3 className="text-xl font-bold text-pakistan-green mb-4 urdu-text">
        گفتگو
      </h3>
      
      {messages.length === 0 ? (
        <div className="text-center text-gray-400 py-8">
          <p className="urdu-text text-lg">کوئی پیغام نہیں ہے</p>
          <p className="text-sm mt-2">Start speaking to see messages here</p>
        </div>
      ) : (
        <div className="space-y-4">
          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}
          <div ref={messagesEndRef} />
        </div>
      )}
    </div>
  );
};

export default ChatWindow;
