Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "             Starting LLM Council                       " -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "`n[1/2] Starting Backend on http://localhost:8001 ..." -ForegroundColor Green
if (Test-Path "$scriptDir\.venv\Scripts\activate.bat") {
    Start-Process cmd.exe -ArgumentList "/k cd /d `"$scriptDir`" && call .venv\Scripts\activate.bat && python -m backend.main"
} else {
    Start-Process cmd.exe -ArgumentList "/k cd /d `"$scriptDir`" && uv run python -m backend.main"
}

Start-Sleep -Seconds 2

Write-Host "[2/2] Starting Frontend on http://localhost:5173 ..." -ForegroundColor Green
Start-Process cmd.exe -ArgumentList "/k cd /d `"$scriptDir\frontend`" && npm run dev"

Start-Sleep -Seconds 2
Start-Process "http://localhost:5173"
Write-Host "`nLLM Council launched! (Backend: http://localhost:8001, Frontend: http://localhost:5173)`n" -ForegroundColor Yellow
