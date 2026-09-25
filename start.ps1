Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "               Starting LLM Council" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "
[1/2] Starting Backend on http://localhost:8001 ..." -ForegroundColor Green
Start-Process cmd.exe -ArgumentList "/k cd /d "$scriptDir" && call .venv\Scripts\activate.bat && python -m backend.main"

Start-Sleep -Seconds 3

Write-Host "[2/2] Starting Frontend on http://localhost:5173 ..." -ForegroundColor Green
Start-Process cmd.exe -ArgumentList "/k cd /d "$scriptDir\frontend" && npm run dev"

Start-Sleep -Seconds 2
Start-Process "http://localhost:5173"
Write-Host "
LLM Council launched! (Backend: :8001, Frontend: :5173)" -ForegroundColor Yellow
