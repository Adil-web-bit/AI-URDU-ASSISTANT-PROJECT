# Urdu Voice Assistant - Complete Startup Script
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Urdu Voice Assistant - Complete Startup" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if running from correct directory
if (-not (Test-Path "backend\main.py")) {
    Write-Host "ERROR: Please run this script from the project root directory!" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[1/4] Starting Backend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\backend; .\.venv\Scripts\Activate.ps1; python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

Write-Host "`n[2/4] Waiting for backend to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

Write-Host "`n[3/4] Starting Frontend Server..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd $PWD\frontend; npm start"

Write-Host "`n[4/4] Opening browser..." -ForegroundColor Yellow
Start-Sleep -Seconds 10
Start-Process "http://localhost:3000"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host " Both servers are starting!" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Yellow
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Yellow
Write-Host "`nPress any key to exit this window..." -ForegroundColor Gray
Write-Host "(Servers will continue running in other windows)" -ForegroundColor Gray
pause
