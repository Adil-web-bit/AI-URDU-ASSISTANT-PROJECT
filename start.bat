@echo off
echo ========================================
echo Urdu Voice Assistant - Complete Startup
echo ========================================
echo.

REM Check if running from correct directory
if not exist "backend\main.py" (
    echo ERROR: Please run this script from the project root directory!
    pause
    exit /b 1
)

echo [1/4] Starting Backend Server...
start "Backend Server" cmd /k "cd backend && .venv\Scripts\activate && python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

echo.
echo [2/4] Waiting for backend to start...
timeout /t 5 /nobreak >nul

echo.
echo [3/4] Starting Frontend Server...
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo [4/4] Opening browser...
timeout /t 10 /nobreak >nul
start http://localhost:3000

echo.
echo ========================================
echo  Both servers are starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this window...
echo (Servers will continue running in other windows)
pause >nul
