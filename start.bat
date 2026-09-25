@echo off
title LLM Council Launcher
echo ========================================================
echo               Starting LLM Council
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/2] Starting Backend on http://localhost:8001 ...
start "LLM Council Backend" cmd /k "call .venv\Scripts\activate.bat && python -m backend.main"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend on http://localhost:5173 ...
start "LLM Council Frontend" cmd /k "cd frontend && npm run dev"

timeout /t 2 /nobreak >nul
echo.
echo Opening browser to http://localhost:5173 ...
start http://localhost:5173

echo.
echo LLM Council is running!
echo Close the backend and frontend command windows to stop.
