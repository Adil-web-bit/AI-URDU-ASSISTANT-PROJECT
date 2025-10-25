# Urdu Voice Assistant Frontend - Start Script
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Starting Urdu Voice Assistant Frontend" -ForegroundColor Green
Write-Host "========================================`n" -ForegroundColor Cyan

Set-Location $PSScriptRoot

Write-Host "[1/2] Checking Node.js..." -ForegroundColor Yellow
$nodeVersion = node --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Node.js not found!" -ForegroundColor Red
    Write-Host "Please install Node.js from: https://nodejs.org/" -ForegroundColor Yellow
    pause
    exit 1
}
Write-Host "   Node.js version: $nodeVersion" -ForegroundColor Green

Write-Host "`n[2/2] Starting React development server..." -ForegroundColor Yellow
Write-Host "   Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "   Backend:  http://localhost:8000 (must be running)" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop the server`n" -ForegroundColor Yellow

npm start
