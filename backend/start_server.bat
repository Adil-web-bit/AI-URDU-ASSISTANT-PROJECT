@echo off
echo ============================================================
echo Starting Urdu Voice Assistant Server
echo ============================================================
echo.
cd /d F:\urdu-voice-assistant\backend
F:\urdu-voice-assistant\.venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
