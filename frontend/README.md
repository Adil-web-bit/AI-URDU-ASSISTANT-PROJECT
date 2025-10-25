# Urdu Voice Assistant - Frontend

Beautiful React frontend for Urdu Voice Assistant with voice input/output capabilities.

## 🚀 Features

- **Voice Input**: Browser-based speech recognition (Web Speech API)
- **Voice Output**: Natural Urdu speech using Google TTS
- **Real-time Chat**: Beautiful conversation interface
- **Quick Commands**: Pre-defined command buttons
- **Responsive Design**: Works on desktop and mobile
- **Pakistan Theme**: Green/white color scheme
- **Urdu Font Support**: Noto Nastaliq Urdu font

## 📋 Prerequisites

- Node.js 14+ and npm
- Backend API running at http://localhost:8000
- Modern browser (Chrome, Edge, Safari recommended)

## 🔧 Installation

### 1. Navigate to frontend directory:
```bash
cd frontend
```

### 2. Install dependencies:
```bash
npm install
```

### 3. Create .env file (optional):
```bash
cp .env.example .env
```

Edit `.env` if backend is on different URL:
```
REACT_APP_API_URL=http://localhost:8000
```

## 🚀 Running the Application

### Development Mode:
```bash
npm start
```

Opens at: **http://localhost:3000**

### Production Build:
```bash
npm run build
```

## 📱 Browser Support

| Browser | Voice Recognition | Audio Playback | Status |
|---------|------------------|----------------|--------|
| Chrome  | ✅ Full Support   | ✅ Yes         | ✅ Recommended |
| Edge    | ✅ Full Support   | ✅ Yes         | ✅ Recommended |
| Firefox | ⚠️ Limited       | ✅ Yes         | ⚠️ Partial |
| Safari  | ⚠️ Limited       | ✅ Yes         | ⚠️ Partial |

**Best Experience**: Google Chrome or Microsoft Edge

## 🎤 Usage

1. **Start Backend**: Make sure backend is running at `http://localhost:8000`
2. **Start Frontend**: Run `npm start`
3. **Open Browser**: Go to `http://localhost:3000`
4. **Click Microphone**: Click the green microphone button
5. **Speak Command**: Say your command in Urdu or English
6. **Listen Response**: Assistant will respond with voice and text

## 📝 Available Commands

### Time & Date
- "What time is it?"
- "What is the date?"
- "وقت کیا ہوا ہے؟"
- "آج کی تاریخ کیا ہے؟"

### Weather
- "What's the weather?"
- "موسم کیسا ہے؟"

### Greetings
- "Hello"
- "السلام علیکم"

### Entertainment
- "Tell me a joke"
- "کوئی لطیفہ سناؤ"

### Help
- "Help"
- "مدد"

## 🎨 Tech Stack

- **React 18**: Modern React with hooks
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API calls
- **Lucide React**: Beautiful icon library
- **Web Speech API**: Browser speech recognition
- **HTML5 Audio**: Audio playback

## 📁 Project Structure

```
frontend/
├── public/
│   └── index.html          # HTML template
├── src/
│   ├── components/         # React components
│   │   ├── Header.jsx
│   │   ├── VoiceInput.jsx
│   │   ├── ChatWindow.jsx
│   │   ├── MessageBubble.jsx
│   │   ├── QuickCommands.jsx
│   │   └── Footer.jsx
│   ├── services/          # Service layer
│   │   ├── api.js
│   │   ├── audioService.js
│   │   └── speechService.js
│   ├── utils/             # Utilities
│   │   └── constants.js
│   ├── App.jsx            # Main app component
│   ├── index.js           # Entry point
│   └── index.css          # Global styles
├── package.json
├── tailwind.config.js
└── README.md
```

## 🔧 Configuration

### API Endpoint
Default: `http://localhost:8000`

To change, edit `.env`:
```
REACT_APP_API_URL=http://your-backend-url:port
```

### Styling
Colors defined in `tailwind.config.js`:
- Pakistan Green: `#01411C`
- Pakistan Light Green: `#0B6623`
- Pakistan Cream: `#F5F5DC`

## 🐛 Troubleshooting

### Microphone Not Working
- Check browser permissions
- Use HTTPS or localhost
- Use Chrome/Edge for best support

### Backend Connection Failed
- Verify backend is running: `http://localhost:8000/health`
- Check CORS settings in backend
- Verify `.env` file configuration

### Audio Not Playing
- Check browser audio permissions
- Verify backend is generating audio files
- Check browser console for errors

## 📦 Build for Production

```bash
npm run build
```

Creates optimized build in `build/` folder.

### Deploy to Netlify/Vercel:
1. Build: `npm run build`
2. Deploy `build/` folder
3. Set environment variable: `REACT_APP_API_URL`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - Free to use and modify

## 👨‍💻 Author

Made with ❤️ in Pakistan

## 🔗 Links

- Backend Repository: [Link]
- Documentation: [Link]
- Demo: [Link]

---

**Happy Coding! 🎉**
