# Urdu Voice Assistant - Backend API

Production-ready FastAPI backend for Urdu Voice Assistant with AI-powered voice command processing.

## 🚀 Features

- **Voice Command Processing**: Understand Urdu/English voice commands
- **Intent Detection**: Regex-based NLP intent classification (11+ intents)
- **Speech Synthesis**: Google TTS (gTTS) - 100% FREE, no API keys needed
- **RESTful API**: Complete REST API with FastAPI
- **Urdu Support**: Native Urdu language processing with UTF-8
- **Real-time Audio**: Generate and serve audio responses instantly
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **CORS Enabled**: Ready for frontend integration
- **Interactive Docs**: Swagger UI and ReDoc documentation
- **Production Ready**: Error handling, validation, security

## 📋 Requirements

- **Python**: 3.10 or higher
- **pip**: Python package manager
- **OS**: Windows, Linux, or macOS

## 🔧 Installation

### 1. Navigate to backend directory:
```bash
cd backend
```

### 2. Create virtual environment (recommended):
```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Verify installation:
```bash
python -c "import fastapi, gtts, uvicorn; print('✅ All dependencies installed!')"
```

## ▶️ Running the Server

### Development Mode (with auto-reload):
```bash
python main.py
```

### Using Uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Production Mode (no auto-reload):
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Custom Port:
```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

### With Multiple Workers (Production):
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🌐 API Endpoints

Server runs at: `http://localhost:8000`

### 📍 Root Endpoint
```http
GET /
```
Returns API information and available endpoints.

**Response:**
```json
{
  "name": "Urdu Voice Assistant",
  "version": "1.0.0",
  "status": "running",
  "message": "اردو وائس اسسٹنٹ - Urdu Voice Assistant API",
  "endpoints": {
    "docs": "/docs",
    "health": "/health",
    "process_command": "/api/v1/process-command"
  }
}
```

---

### 🏥 Health Check
```http
GET /health
```
Check if the API is healthy and running.

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2025-10-25T12:00:00"
}
```

---

### 🎤 Process Voice Command
```http
POST /api/v1/process-command
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "السلام علیکم، کیا حال ہے؟",
  "user_id": "user_123",
  "language": "auto"
}
```

**Response:**
```json
{
  "response_text": "السلام علیکم! میں ٹھیک ہوں، شکریہ۔",
  "audio_file": "speech_20251025_120000_123456.mp3",
  "intent": "greeting",
  "confidence": 0.95,
  "language": "ur",
  "timestamp": "2025-10-25T12:00:00"
}
```

---

### 🔊 Get Audio File
```http
GET /api/v1/audio/{filename}
```

**Example:**
```http
GET /api/v1/audio/speech_20251025_120000_123456.mp3
```

**Response:** MP3 audio file

---

### 📋 Get Available Commands
```http
GET /api/v1/commands
```

**Response:**
```json
{
  "commands": [
    {
      "category": "greeting",
      "examples": ["سلام", "ہیلو", "آداب", "السلام علیکم"],
      "description": "اردو وائس اسسٹنٹ سے بات شروع کریں"
    },
    {
      "category": "weather",
      "examples": ["موسم کیسا ہے؟", "آج کا موسم", "بارش ہو گی؟"],
      "description": "موسم کی معلومات حاصل کریں"
    }
  ],
  "total": 8
}
```

---

### 🎯 Get Supported Intents
```http
GET /api/v1/intents
```

**Response:**
```json
{
  "intents": ["greeting", "farewell", "thanks", "weather", "time", "date", "prayer", "joke", "news", "help", "unknown"],
  "total": 11,
  "message": "دستیاب intents کی فہرست"
}
```

---

### 🧪 Test Speech Generation
```http
POST /api/v1/test-speech?text=ہیلو دنیا&lang=ur
```

**Response:**
```json
{
  "message": "Speech generated successfully",
  "audio_file": "speech_xxx.mp3",
  "text": "ہیلو دنیا",
  "language": "ur",
  "audio_url": "/api/v1/audio/speech_xxx.mp3"
}
```

---

### 📊 Get Statistics
```http
GET /api/v1/stats
```

**Response:**
```json
{
  "audio_files_generated": 42,
  "total_audio_size_mb": 12.5,
  "supported_languages": ["ur", "en"],
  "supported_intents": 11,
  "api_version": "1.0.0",
  "status": "operational"
}
```

## 📖 API Documentation

Interactive API documentation available at:

- **Swagger UI**: http://localhost:8000/docs
  - Interactive API explorer
  - Try out endpoints directly
  - View request/response schemas

- **ReDoc**: http://localhost:8000/redoc
  - Clean, readable documentation
  - Detailed endpoint descriptions
  - Example requests and responses

## 🎯 Supported Intents

| Intent | Description | Example Commands |
|--------|-------------|------------------|
| **greeting** | Greetings and hellos | سلام، ہیلو، آداب |
| **farewell** | Goodbyes | اللہ حافظ، bye، الوداع |
| **thanks** | Thank you messages | شکریہ، thanks، مہربانی |
| **how_are_you** | How are you queries | کیسے ہو، حال کیسا ہے |
| **weather** | Weather queries (mock) | موسم کیسا ہے؟ |
| **time** | Current time | وقت کیا ہوا ہے؟ |
| **date** | Current date | آج کی تاریخ کیا ہے؟ |
| **prayer** | Prayer times (mock) | نماز کا وقت |
| **joke** | Urdu jokes | لطیفہ سناؤ |
| **news** | News headlines (mock) | تازہ خبریں |
| **help** | Help and commands list | مدد، help |

## 📁 Project Structure

```
backend/
├── main.py                 # FastAPI application (SEGMENT 3)
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── test_services.py        # Service testing script
├── README.md               # This file
│
├── services/               # Business logic (SEGMENT 2)
│   ├── __init__.py
│   ├── command_service.py      # Main orchestration
│   ├── intent_detector.py      # Intent classification
│   ├── response_generator.py   # Response generation
│   └── speech_service.py       # Text-to-speech
│
├── models/                 # Data models (SEGMENT 1)
│   ├── __init__.py
│   └── schemas.py              # Pydantic models
│
├── utils/                  # Utilities (SEGMENT 1)
│   ├── __init__.py
│   ├── helpers.py              # Helper functions
│   └── logger.py               # Logging setup
│
├── data/                   # JSON data (SEGMENT 1)
│   ├── responses.json          # Response templates
│   ├── jokes.json              # Urdu jokes
│   ├── commands.json           # Command examples
│   └── patterns.json           # Intent patterns
│
├── audio_outputs/          # Generated audio files
│   └── .gitkeep
│
└── logs/                   # Application logs
    └── .gitkeep
```

## 🔍 Testing

### Test Health Endpoint:
```bash
curl http://localhost:8000/health
```

### Test Command Processing:
```bash
curl -X POST http://localhost:8000/api/v1/process-command \
  -H "Content-Type: application/json" \
  -d '{"text": "سلام", "language": "ur"}'
```

### Test Speech Generation:
```bash
curl -X POST "http://localhost:8000/api/v1/test-speech?text=ہیلو&lang=ur"
```

### Test with Python:
```python
import requests

# Process command
response = requests.post(
    'http://localhost:8000/api/v1/process-command',
    json={'text': 'وقت کیا ہوا ہے؟', 'language': 'ur'}
)
print(response.json())
```

### Run Test Suite:
```bash
python test_services.py
```

## 📝 Logging

Logs are automatically saved in the `logs/` directory:

- **Format**: `assistant_YYYYMMDD.log`
- **Level**: INFO (configurable in `config.py`)
- **Output**: Both console and file
- **Encoding**: UTF-8 (supports Urdu text)

### View Logs:
```bash
# Real-time log viewing (Linux/Mac)
tail -f logs/assistant_*.log

# View latest log (Windows PowerShell)
Get-Content logs\assistant_*.log -Wait

# View specific log file
cat logs/assistant_20251025.log
```

## 🛠️ Configuration

Edit `config.py` to customize:

```python
# Server Settings
HOST = "0.0.0.0"
PORT = 8000
RELOAD = True  # Set False in production

# CORS Settings
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

# Audio Settings
MAX_AUDIO_FILES = 100
AUDIO_FORMAT = "mp3"

# Speech Settings
DEFAULT_LANGUAGE = "ur"

# Logging
LOG_LEVEL = "INFO"
```

## ⚠️ Troubleshooting

### Port Already in Use:
```bash
# Use different port
uvicorn main:app --port 8001
```

### Import Errors:
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Audio Not Generating:
```bash
# Test gTTS directly
python -c "from gtts import gTTS; tts = gTTS('test', lang='ur'); print('✅ gTTS working')"
```

### Permission Errors on Audio Folder:
```bash
# Fix permissions (Linux/Mac)
chmod 755 audio_outputs/

# On Windows, check folder permissions in Properties
```

### CORS Errors:
Add your frontend URL to `CORS_ORIGINS` in `config.py`:
```python
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",  # Add your frontend URL
]
```

## 🚀 Deployment

### Using Gunicorn (Production - Linux):
```bash
# Install gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

### Using Docker:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t urdu-voice-assistant .
docker run -p 8000:8000 urdu-voice-assistant
```

### Environment Variables:
```bash
# Set in production
export DEBUG=False
export HOST=0.0.0.0
export PORT=8000
```

## 📊 Performance

- **Average Response Time**: < 2 seconds
- **Audio Generation**: < 1 second
- **Concurrent Requests**: Supported (async)
- **Auto Cleanup**: Keeps max 100 audio files
- **Memory Efficient**: Streams audio files

## 🔒 Security

- ✅ Input validation on all endpoints
- ✅ Path traversal prevention
- ✅ File type validation (MP3 only)
- ✅ CORS configuration
- ✅ Error message sanitization
- ✅ Request size limits (500 chars for commands)

## 🤝 Contributing

This is an educational/portfolio project. Feel free to:
- Add new intents and responses
- Improve intent detection accuracy
- Add more Urdu jokes
- Optimize performance
- Add new features

## 📄 License

MIT License - Free to use and modify

## 👨‍💻 Author

Built with ❤️ for Pakistani Urdu speakers (220M+ potential users)

## 🙏 Acknowledgments

- **FastAPI**: Modern Python web framework
- **gTTS**: Free Google Text-to-Speech
- **Uvicorn**: Lightning-fast ASGI server

---

## 📞 Need Help?

- Check the **Interactive API Docs**: http://localhost:8000/docs
- View **Test Suite**: `python test_services.py`
- Check **Logs**: `logs/assistant_YYYYMMDD.log`
- Review **Config**: `config.py`

---

**🎉 Ready to use! Start the server and visit `/docs` for interactive API exploration!**
