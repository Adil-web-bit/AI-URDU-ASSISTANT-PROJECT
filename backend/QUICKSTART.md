# Urdu Voice Assistant - Quick Start Guide

## 🚀 Quick Start (SEGMENT 3 - FastAPI Server)

### Step 1: Start the Server
```bash
cd backend
python main.py
```

You should see:
```
============================================================
🚀 Urdu Voice Assistant
============================================================
📡 Host: 0.0.0.0
🔌 Port: 8000
📖 Docs: http://0.0.0.0:8000/docs
============================================================
```

### Step 2: Open API Documentation
Visit: **http://localhost:8000/docs**

This opens the interactive Swagger UI where you can:
- ✅ View all endpoints
- ✅ Test API calls directly
- ✅ See request/response examples

### Step 3: Test the API

#### Option A: Use the Interactive Docs
1. Go to http://localhost:8000/docs
2. Click on `POST /api/v1/process-command`
3. Click "Try it out"
4. Enter:
   ```json
   {
     "text": "السلام علیکم",
     "language": "ur"
   }
   ```
5. Click "Execute"
6. See the response with audio file!

#### Option B: Use curl (Command Line)
```bash
# Test health
curl http://localhost:8000/health

# Process a command
curl -X POST http://localhost:8000/api/v1/process-command \
  -H "Content-Type: application/json" \
  -d '{"text": "سلام", "language": "ur"}'
```

#### Option C: Use Python
```python
import requests

# Process command
response = requests.post(
    'http://localhost:8000/api/v1/process-command',
    json={'text': 'وقت کیا ہوا ہے؟', 'language': 'ur'}
)

result = response.json()
print(f"Intent: {result['intent']}")
print(f"Response: {result['response_text']}")
print(f"Audio: {result['audio_file']}")
```

#### Option D: Run Test Suite
```bash
# Start server in one terminal
python main.py

# In another terminal, run tests
python test_api.py
```

### Step 4: Download Generated Audio
After processing a command, you'll get an audio file name like:
```
speech_20251025_120000_123456.mp3
```

Access it at:
```
http://localhost:8000/api/v1/audio/speech_20251025_120000_123456.mp3
```

Or directly in browser:
```
http://localhost:8000/audio/speech_20251025_120000_123456.mp3
```

## 📍 Important Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API info |
| `/health` | GET | Health check |
| `/docs` | GET | Swagger UI |
| `/api/v1/process-command` | POST | Process voice command |
| `/api/v1/audio/{filename}` | GET | Get audio file |
| `/api/v1/commands` | GET | List commands |
| `/api/v1/intents` | GET | List intents |
| `/api/v1/test-speech` | POST | Test TTS |
| `/api/v1/stats` | GET | Get statistics |

## 🎯 Example Commands to Test

Try these Urdu commands:

1. **Greeting**: `السلام علیکم`
2. **Time**: `وقت کیا ہوا ہے؟`
3. **Date**: `آج کی تاریخ کیا ہے؟`
4. **Weather**: `موسم کیسا ہے؟`
5. **Joke**: `کوئی لطیفہ سناؤ`
6. **Prayer**: `نماز کا وقت`
7. **News**: `تازہ خبریں`
8. **Help**: `مدد`

## 🔍 Troubleshooting

### Server won't start?
```bash
# Check if port 8000 is already in use
netstat -ano | findstr :8000

# Use different port
uvicorn main:app --port 8001
```

### Import errors?
```bash
pip install -r requirements.txt --force-reinstall
```

### Can't access from browser?
- Make sure server is running
- Check firewall settings
- Try http://127.0.0.1:8000 instead of localhost

## 📖 Full Documentation

See **README.md** for complete documentation including:
- All API endpoints
- Request/response examples
- Configuration options
- Deployment instructions
- Security best practices

## 🎉 Next Steps

After SEGMENT 3 is complete and working:
1. ✅ Backend API is ready
2. ⏭️ **SEGMENT 4**: Build React frontend
3. ⏭️ **SEGMENT 5**: Integration & deployment

---

**Need help? Visit http://localhost:8000/docs for interactive API exploration!**
