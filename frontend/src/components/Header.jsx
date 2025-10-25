import React from 'react';
import { Mic } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-gradient-to-r from-pakistan-green to-pakistan-lightgreen text-white shadow-lg">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="bg-white p-3 rounded-full shadow-lg">
              <Mic className="w-8 h-8 text-pakistan-green" />
            </div>
            <div>
              <h1 className="text-2xl md:text-3xl font-bold">
                اردو وائس اسسٹنٹ
              </h1>
              <p className="text-sm text-pakistan-cream opacity-90">
                AI-Powered Urdu Voice Assistant
              </p>
            </div>
          </div>
          <div className="hidden md:block">
            <div className="flex items-center space-x-4">
              <span className="text-sm opacity-75">Made with ❤️ in Pakistan</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
