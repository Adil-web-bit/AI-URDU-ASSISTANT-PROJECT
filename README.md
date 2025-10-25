# اردو وائس اسسٹنٹ - Urdu Voice Assistant

<div align="center">

![Made in Pakistan](https://img.shields.io/badge/Made%20in-Pakistan-green?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18.0+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**AI-Powered Voice Assistant with Natural Urdu Speech**

[Features](#-features) • [Quick Start](#-quick-start-5-minutes) • [Demo](#-demo) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

### 🎤 **Voice Recognition**
- Browser-based speech recognition (Web Speech API)
- Supports **Urdu** and **English** languages
- Real-time transcription with confidence scoring
- No API keys or paid services required

### 🔊 **Natural Speech Output**
- Google Text-to-Speech (gTTS) for Urdu responses
- Automatic audio generation and playback
- Natural-sounding Urdu voice
- MP3 audio format with browser playback

### 🧠 **Intelligent Command Processing**
- **8 Command Categories:**
  - 👋 Greetings (سلام، خوش آمدید)
  - 🌤️ Weather (موسم، بارش)
  - ⏰ Time (وقت کیا ہے؟)
  - 📅 Date (آج کی تاریخ)
  - 🕌 Prayer Times (نماز کا وقت)
  - 🎭 Entertainment (لطیفے، jokes)
  - 📰 News (خبریں)
  - ❓ Help (مدد)

### 🇵🇰 **Beautiful Pakistan-Themed UI**
- Green and white color scheme (Pakistan flag colors)
- Noto Nastaliq Urdu font (Google Fonts)
- Responsive design (mobile, tablet, desktop)
- Real-time chat interface
- Quick command buttons
- Connection status monitoring

### 💯 **100% Free & Open Source**
- No API keys required
- No subscription fees
- No external paid services
- MIT License

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           REACT FRONTEND (Port 3000)                 │  │
│  │  ┌────────────┐  ┌────────────┐  ┌──────────────┐  │  │
│  │  │  Voice     │  │   Chat     │  │    Quick     │  │  │
│  │  │  Input     │  │  Window    │  │   Commands   │  │  │
│  │  └────────────┘  └────────────┘  └──────────────┘  │  │
│  │         │                │                │          │  │
│  │         └────────────────┴────────────────┘          │  │
│  │                      │                                │  │
│  │               Web Speech API                          │  │
│  │                      │                                │  │
│  └──────────────────────┼────────────────────────────────┘  │
│                         │                                    │
│                    HTTP/REST API                             │
│                         │                                    │
└─────────────────────────┼────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│               PYTHON BACKEND (Port 8000)                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  FastAPI Server                       │  │
│  │  ┌────────────┐  ┌────────────┐  ┌──────────────┐  │  │
│  │  │  Intent    │  │ Response   │  │   Speech     │  │  │
│  │  │ Detector   │→│ Generator  │→│   Service    │  │  │
│  │  └────────────┘  └────────────┘  └──────────────┘  │  │
│  │         │                │                │          │  │
│  │         └────────────────┴────────────────┘          │  │
│  │                      │                                │  │
│  │               Command Service                          │  │
│  │                      │                                │  │
│  └──────────────────────┼────────────────────────────────┘  │
│                         │                                    │
│                    ┌────┴────┐                              │
│                    │  gTTS   │                              │
│                    │  (TTS)  │                              │
│                    └─────────┘                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### **Backend**
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Core language |
| FastAPI | 0.104.1 | REST API framework |
| gTTS | 2.4.0 | Text-to-Speech (FREE) |
| Pydantic | 2.5.0 | Data validation |
| Uvicorn | 0.24.0 | ASGI server |

### **Frontend**
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2.0 | UI framework |
| Tailwind CSS | 3.3.5 | Styling |
| Axios | 1.6.2 | HTTP client |
| Lucide React | 0.263.1 | Icons |
| Web Speech API | Native | Voice recognition |

### **AI/NLP**
- **Intent Detection**: Regex-based pattern matching
- **Entity Extraction**: Custom extractors for dates, numbers, locations
- **Response Generation**: Template-based with dynamic data
- **Confidence Scoring**: Pattern match strength calculation

---

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.10 or higher** ([Download](https://www.python.org/downloads/))
- ✅ **Node.js 14 or higher** ([Download](https://nodejs.org/))
- ✅ **Modern Browser** (Chrome, Edge, or Firefox - Chrome recommended)
- ✅ **Microphone** (for voice input)
- ✅ **Internet Connection** (for Google TTS API)
- ✅ **Windows/Linux/macOS** (any OS with Python & Node.js)

---

## 🚀 Quick Start (5 Minutes)

### **Step 1: Clone Repository**
```bash
git clone https://github.com/yourusername/urdu-voice-assistant.git
cd urdu-voice-assistant
```

### **Step 2: Setup Backend** ⚙️
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate
# Or on Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

✅ **Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

### **Step 3: Setup Frontend** 🎨
Open a **NEW terminal** window:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start frontend server
npm start
```

✅ **Expected Output:**
```
Compiled successfully!
You can now view the app in the browser.
Local: http://localhost:3000
```

### **Step 4: Test It!** 🎤
1. Browser will open at http://localhost:3000
2. You'll see "Backend Connected" ✅ at the top
3. Click the green **microphone button** 🎤
4. Allow microphone permission when prompted
5. Say: **"Hello"** or **"سلام"**
6. Listen to the Urdu response! 🔊

---

## 📦 Detailed Installation

### **Backend Setup (Detailed)**

1. **Create Virtual Environment:**
```bash
cd backend
python -m venv venv
```

2. **Activate Virtual Environment:**

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

Expected packages:
- fastapi==0.104.1
- uvicorn==0.24.0
- gtts==2.4.0
- pydantic==2.5.0
- python-multipart==0.0.6

4. **Verify Installation:**
```bash
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"
python -c "import gtts; print('gTTS installed successfully')"
```

5. **Start Server:**
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

6. **Test Backend:**
Open browser: http://127.0.0.1:8000/docs

---

### **Frontend Setup (Detailed)**

1. **Install Node.js Dependencies:**
```bash
cd frontend
npm install
```

This installs ~1,327 packages including:
- react, react-dom
- tailwindcss
- axios
- lucide-react

2. **Verify Installation:**
```bash
npm list react
npm list tailwindcss
```

3. **Start Development Server:**
```bash
npm start
```

4. **Build for Production (Optional):**
```bash
npm run build
```

Creates optimized build in `build/` folder.

---

## 📖 Usage Guide

### **Basic Usage**

1. **Start Both Servers** (backend + frontend)
2. **Open Browser:** http://localhost:3000
3. **Check Connection:** Look for "Backend Connected" ✅
4. **Click Microphone:** Green button in center
5. **Allow Permissions:** Grant microphone access
6. **Speak Command:** Say your command clearly
7. **Listen Response:** Urdu audio will play automatically
8. **View Chat:** Messages appear in chat window

---

### **Supported Commands**

#### 👋 **Greetings**
| Urdu | English | Response |
|------|---------|----------|
| السلام علیکم | Hello | وعلیکم السلام! کیسے ہیں؟ |
| خوش آمدید | Welcome | خوش آمدید! میں آپ کی مدد کے لیے حاضر ہوں |
| صبح بخیر | Good morning | صبح بخیر! آپ کا دن مبارک ہو |

#### 🌤️ **Weather**
| Command | Response |
|---------|----------|
| موسم کیسا ہے؟ | آج موسم بہت اچھا ہے! درجہ حرارت 25 ڈگری ہے |
| What's the weather? | آج بارش کا امکان ہے، چھتری ساتھ رکھیں! |
| کیا بارش ہو گی؟ | جی ہاں، آج شام کو بارش کا امکان ہے |

#### ⏰ **Time**
| Command | Response |
|---------|----------|
| وقت کیا ہوا ہے؟ | ابھی 3:45 دوپہر بجے ہیں |
| What time is it? | ابھی 10:30 صبح ہیں |
| ٹائم بتاؤ | اس وقت 8:15 شام ہیں |

#### 📅 **Date**
| Command | Response |
|---------|----------|
| آج کی تاریخ کیا ہے؟ | آج ہفتہ، 25 اکتوبر 2025 ہے |
| What is the date? | آج 25 اکتوبر 2025 ہے |
| تاریخ بتاؤ | آج کی تاریخ ہے 25 اکتوبر |

#### 🕌 **Prayer Times**
| Command | Response |
|---------|----------|
| نماز کا وقت کیا ہے؟ | فجر 5:30، ظہر 12:15، عصر 3:45، مغرب 6:00، عشاء 7:30 |
| فجر کی نماز کا وقت | فجر کی نماز کا وقت 5:30 صبح ہے |

#### 🎭 **Entertainment**
| Command | Response |
|---------|----------|
| کوئی لطیفہ سناؤ | مریض: ڈاکٹر صاحب، مجھے نیند نہیں آتی! ... |
| Tell me a joke | استاد: بچو، آسمان نیلا کیوں ہے؟ ... |

#### 📰 **News**
| Command | Response |
|---------|----------|
| خبریں سناؤ | افسوس! میں ابھی خبریں نہیں دے سکتا |
| Latest news | میں خبروں کی سروس پر کام کر رہا ہوں |

#### ❓ **Help**
| Command | Response |
|---------|----------|
| مدد | میں آپ کی مدد کے لیے حاضر ہوں! ... |
| Help | I can help you with weather, time, prayers, and more! |

---

## 🎯 Project Structure

```
urdu-voice-assistant/
├── backend/                    # Python FastAPI Backend
│   ├── config/                # Configuration files
│   │   ├── __init__.py
│   │   └── settings.py        # App settings
│   ├── models/                # Pydantic models
│   │   ├── __init__.py
│   │   ├── request.py         # Request schemas
│   │   └── response.py        # Response schemas
│   ├── services/              # Business logic
│   │   ├── __init__.py
│   │   ├── speech_service.py  # gTTS integration
│   │   ├── intent_detector.py # Intent detection
│   │   ├── response_generator.py # Response generation
│   │   └── command_service.py # Main orchestrator
│   ├── data/                  # Static data
│   │   ├── patterns.json      # Intent patterns
│   │   ├── responses.json     # Response templates
│   │   └── jokes.json         # Joke database
│   ├── audio_outputs/         # Generated audio files
│   ├── logs/                  # Application logs
│   ├── main.py               # FastAPI app entry point
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # Backend documentation
│
├── frontend/                  # React Frontend
│   ├── public/
│   │   └── index.html        # HTML template
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── Header.jsx
│   │   │   ├── VoiceInput.jsx
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── MessageBubble.jsx
│   │   │   ├── QuickCommands.jsx
│   │   │   └── Footer.jsx
│   │   ├── services/         # API services
│   │   │   ├── api.js
│   │   │   ├── audioService.js
│   │   │   └── speechService.js
│   │   ├── utils/
│   │   │   └── constants.js  # Constants
│   │   ├── App.jsx           # Main app component
│   │   ├── index.js          # Entry point
│   │   └── index.css         # Global styles
│   ├── package.json          # Node dependencies
│   ├── tailwind.config.js    # Tailwind config
│   └── README.md             # Frontend documentation
│
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .gitignore                # Git ignore rules
```

**Total Files:** 60+ files  
**Total Code:** 4,500+ lines  
**Backend:** 2,000+ lines (Python)  
**Frontend:** 2,000+ lines (JavaScript/JSX)  
**Configuration:** 500+ lines (JSON/config)

---

## 🧪 Testing

### **Backend API Testing**

1. **Health Check:**
```bash
curl http://127.0.0.1:8000/health
```

Expected:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-10-25T12:00:00"
}
```

2. **Process Command:**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/process-command \
  -H "Content-Type: application/json" \
  -d '{"text":"hello","language":"en"}'
```

Expected:
```json
{
  "response_text": "السلام علیکم و رحمۃ اللہ! کیسے ہیں؟",
  "audio_file": "speech_20251025_120000_123456.mp3",
  "intent": "greeting",
  "confidence": 0.95,
  "language": "en",
  "timestamp": "2025-10-25T12:00:00"
}
```

3. **Get Commands:**
```bash
curl http://127.0.0.1:8000/api/v1/commands
```

4. **API Documentation:**
Open browser: http://127.0.0.1:8000/docs

### **Frontend Testing**

1. **Open App:** http://localhost:3000
2. **Check Connection:** Backend Connected ✅
3. **Click Microphone:** Allow permissions
4. **Test Commands:**
   - Say "Hello"
   - Say "What time is it?"
   - Say "Weather"
   - Click quick command buttons

### **Unit Tests**

Run backend tests:
```bash
cd backend
python test_services.py
```

Expected output:
```
✅ Testing IntentDetector...
✅ Testing ResponseGenerator...
✅ Testing SpeechService...
✅ Testing CommandService...
All tests passed!
```

---

## 🐛 Troubleshooting

### **Backend Issues**

#### Port Already in Use
```bash
# Kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

#### gTTS Not Working
```bash
# Reinstall gTTS
pip uninstall gtts
pip install gtts==2.4.0

# Test
python -c "from gtts import gTTS; gTTS('test', lang='ur').save('test.mp3')"
```

#### Dependencies Error
```bash
# Clean install
rm -rf venv
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### **Frontend Issues**

#### npm install fails
```bash
# Clear cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

#### Port 3000 in use
```bash
# Change port (set before npm start)
set PORT=3001  # Windows
export PORT=3001  # Linux/Mac
npm start
```

#### Microphone not working
- Use **Chrome** or **Edge** browser (best support)
- Check browser microphone permissions
- Use HTTPS or localhost (required for Web Speech API)
- Check if microphone is working in OS settings

#### Backend not connecting
- Verify backend is running: http://127.0.0.1:8000/health
- Check CORS settings in backend
- Click "Retry Connection" button
- Check browser console for errors (F12)

---

## 🚀 Deployment

### **Backend Deployment**

#### **Option 1: Local Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### **Option 2: Docker**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### **Option 3: Heroku/Railway**
- Add `Procfile`: `web: uvicorn main:app --host 0.0.0.0 --port $PORT`
- Push to repository
- Deploy

### **Frontend Deployment**

#### **Option 1: Netlify**
```bash
npm run build
# Deploy build/ folder to Netlify
```

#### **Option 2: Vercel**
```bash
npm run build
vercel --prod
```

#### **Option 3: GitHub Pages**
```bash
npm run build
# Deploy build/ folder to gh-pages branch
```

**Remember:** Update `REACT_APP_API_URL` in `.env` with production backend URL!

---

## 📊 Performance

### **Metrics**

| Metric | Value |
|--------|-------|
| Backend Response Time | < 500ms |
| Audio Generation Time | < 2 seconds |
| Frontend Load Time | < 3 seconds |
| Memory Usage (Backend) | ~50-100 MB |
| Memory Usage (Frontend) | ~80-150 MB |
| Audio File Size | ~10-50 KB per response |

### **Optimization Tips**

- **Backend:**
  - Use Redis for caching responses
  - Implement audio file cleanup (delete old files)
  - Use async/await for non-blocking operations
  - Add rate limiting for API endpoints

- **Frontend:**
  - Lazy load components
  - Implement service workers for PWA
  - Compress images and assets
  - Use React.memo for heavy components

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the Repository**
```bash
git clone https://github.com/yourusername/urdu-voice-assistant.git
```

2. **Create Feature Branch**
```bash
git checkout -b feature/amazing-feature
```

3. **Commit Changes**
```bash
git commit -m "Add amazing feature"
```

4. **Push to Branch**
```bash
git push origin feature/amazing-feature
```

5. **Open Pull Request**

### **Contribution Guidelines**
- Follow PEP 8 (Python) and Airbnb (JavaScript) style guides
- Add tests for new features
- Update documentation
- Keep commits atomic and descriptive
- Be respectful and collaborative

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Urdu Voice Assistant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

**Made with ❤️ in Pakistan**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourname)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- **Google Text-to-Speech (gTTS)** - Free TTS service
- **Web Speech API** - Browser voice recognition
- **FastAPI** - Modern Python web framework
- **React** - JavaScript UI library
- **Tailwind CSS** - Utility-first CSS framework
- **Lucide Icons** - Beautiful icon library
- **Noto Nastaliq Urdu Font** - Google Fonts

---

## 📞 Support

Having issues? We're here to help!

- 📖 [Documentation](./docs/)
- 🐛 [Report Bug](https://github.com/yourusername/urdu-voice-assistant/issues)
- 💡 [Request Feature](https://github.com/yourusername/urdu-voice-assistant/issues)
- 💬 [Discussions](https://github.com/yourusername/urdu-voice-assistant/discussions)

---

## 🗺️ Roadmap

### **Version 1.1** (Coming Soon)
- [ ] Urdu keyboard input support
- [ ] More joke categories
- [ ] Weather API integration (real data)
- [ ] Prayer times API integration
- [ ] Voice customization (speed, pitch)

### **Version 2.0** (Future)
- [ ] Mobile app (React Native)
- [ ] Offline mode support
- [ ] Custom wake word ("Hey Assistant")
- [ ] Multi-user support
- [ ] Conversation history
- [ ] Advanced NLP (transformers)
- [ ] Integration with smart home devices

---

## ⭐ Star History

If you find this project useful, please consider giving it a ⭐ star on GitHub!

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/urdu-voice-assistant?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/urdu-voice-assistant?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/urdu-voice-assistant)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/urdu-voice-assistant)

---

<div align="center">

**Built with 💚 for the Urdu-speaking community**

**اردو بولنے والوں کے لیے محبت سے بنایا گیا**

[⬆ Back to Top](#اردو-وائس-اسسٹنٹ---urdu-voice-assistant)

</div>
