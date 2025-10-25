# Start Server Script
# Run this to start the FastAPI server

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Starting Urdu Voice Assistant Server" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Set-Location -Path "F:\urdu-voice-assistant\backend"
& "F:\urdu-voice-assistant\.venv\Scripts\python.exe" -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
