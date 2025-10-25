import React from 'react';
import { 
  CloudSun, 
  Clock, 
  Calendar,
  Laugh, 
  Hand,
  HelpCircle 
} from 'lucide-react';
import { QUICK_COMMANDS } from '../utils/constants';

const iconMap = {
  CloudSun,
  Clock,
  Calendar,
  Laugh,
  Hand,
  HelpCircle
};

const QuickCommands = ({ onCommandClick, disabled }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h3 className="text-xl font-bold text-pakistan-green mb-4 urdu-text">
        فوری کمانڈز
      </h3>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {QUICK_COMMANDS.map((cmd) => {
          const Icon = iconMap[cmd.icon];
          return (
            <button
              key={cmd.id}
              onClick={() => onCommandClick(cmd.command)}
              disabled={disabled}
              className="
                hover-card
                bg-gradient-to-br from-pakistan-cream to-white
                border-2 border-pakistan-green
                rounded-xl p-4
                flex flex-col items-center justify-center
                space-y-2
                transition-all duration-300
                hover:shadow-xl
                disabled:opacity-50 disabled:cursor-not-allowed
                focus:outline-none focus:ring-2 focus:ring-pakistan-lightgreen
              "
            >
              <Icon className="w-8 h-8 text-pakistan-green" />
              <span className="text-sm font-medium text-pakistan-green urdu-text text-center">
                {cmd.text}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};

export default QuickCommands;
