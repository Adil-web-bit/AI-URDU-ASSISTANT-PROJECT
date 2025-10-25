@echo off
echo ========================================
echo Starting Urdu Voice Assistant Frontend
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] Checking Node.js...
node --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Node.js not found!
    pause
    exit /b 1
)

echo.
echo [2/2] Starting React development server...
echo Frontend will open at: http://localhost:3000
echo Make sure backend is running at: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

npm start

pause
