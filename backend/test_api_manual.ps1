# PowerShell Script to Test Urdu Voice Assistant API
# Save as: test_api_manual.ps1

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "Testing Urdu Voice Assistant API" -ForegroundColor Green
Write-Host "============================================================`n" -ForegroundColor Cyan

$baseUrl = "http://127.0.0.1:8000"

# Test 1: Root Endpoint
Write-Host "1. Testing Root Endpoint..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/" -Method Get
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Name: $($response.name)" -ForegroundColor White
    Write-Host "   Version: $($response.version)" -ForegroundColor White
    Write-Host "   Status: $($response.status)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

# Test 2: Health Check
Write-Host "2. Testing Health Check..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/health" -Method Get
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Status: $($response.status)" -ForegroundColor White
    Write-Host "   Version: $($response.version)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

# Test 3: Process Command (Greeting)
Write-Host "3. Testing Voice Command (Greeting)..." -ForegroundColor Yellow
try {
    $body = @{
        text = "السلام علیکم"
        language = "ur"
    } | ConvertTo-Json -Compress

    $response = Invoke-RestMethod -Uri "$baseUrl/api/v1/process-command" -Method Post -Body $body -ContentType "application/json"
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Intent: $($response.intent)" -ForegroundColor White
    Write-Host "   Confidence: $($response.confidence)" -ForegroundColor White
    Write-Host "   Response: $($response.response_text)" -ForegroundColor White
    Write-Host "   Audio File: $($response.audio_file)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

# Test 4: Process Command (Time)
Write-Host "4. Testing Voice Command (Time)..." -ForegroundColor Yellow
try {
    $body = @{
        text = "وقت کیا ہوا ہے؟"
        language = "ur"
    } | ConvertTo-Json -Compress

    $response = Invoke-RestMethod -Uri "$baseUrl/api/v1/process-command" -Method Post -Body $body -ContentType "application/json"
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Intent: $($response.intent)" -ForegroundColor White
    Write-Host "   Response: $($response.response_text)" -ForegroundColor White
    Write-Host "   Audio File: $($response.audio_file)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

# Test 5: Get Commands List
Write-Host "5. Testing Commands List..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/v1/commands" -Method Get
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Total Commands: $($response.total)" -ForegroundColor White
    Write-Host "   First Command: $($response.commands[0].category)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

# Test 6: Get Statistics
Write-Host "6. Testing Statistics..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/v1/stats" -Method Get
    Write-Host "   ✅ Success!" -ForegroundColor Green
    Write-Host "   Audio Files: $($response.audio_files_generated)" -ForegroundColor White
    Write-Host "   Total Size: $($response.total_audio_size_mb) MB" -ForegroundColor White
    Write-Host "   Supported Intents: $($response.supported_intents)`n" -ForegroundColor White
} catch {
    Write-Host "   ❌ Failed: $_`n" -ForegroundColor Red
}

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "✅ All Tests Complete!" -ForegroundColor Green
Write-Host "============================================================`n" -ForegroundColor Cyan

Write-Host "📖 View API Docs: http://127.0.0.1:8000/docs" -ForegroundColor Yellow
Write-Host "🎤 Process Command: POST http://127.0.0.1:8000/api/v1/process-command`n" -ForegroundColor Yellow
