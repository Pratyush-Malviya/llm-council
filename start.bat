@echo off
title LLM Council
echo ========================================================
echo               Starting LLM Council
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/2] Starting Backend on http://localhost:8001...
if exist ".venv\Scripts\activate.bat" (
    start "LLM Council - Backend (Port 8001)" cmd /k "call .venv\Scripts\activate.bat && python -m backend.main"
) else (
    start "LLM Council - Backend (Port 8001)" cmd /k "uv run python -m backend.main"
)

timeout /t 2 /nobreak >nul

echo [2/2] Starting React Vite Frontend on http://localhost:5173...
cd frontend
start "LLM Council - Frontend (Port 5173)" cmd /k "npm run dev"

echo.
echo ========================================================
echo  LLM Council is now running!
echo  Backend:  http://localhost:8001
echo  Frontend: http://localhost:5173
echo ========================================================
echo.
echo Opening browser to http://localhost:5173...
start http://localhost:5173
