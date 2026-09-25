---
name: llm-council
version: 1.0.0
description: "Consult the Karpathy LLM Council multi-agent deliberation framework to debate, peer-review, and synthesize answers using multiple frontier models (GPT, Claude, Gemini, Grok)."
homepage: https://github.com/karpathy/llm-council
metadata: {"category":"reasoning","provider":"OpenRouter"}
---

# LLM Council 🏛️

The **LLM Council** is a multi-agent deliberation system created by Andrej Karpathy. Instead of relying on a single AI model (which can have blind spots or biases), it sends the query to a council of diverse frontier LLMs, performs an **anonymized peer review** where models critique and rank each other's responses, and has a **Chairman** synthesize the final verdict.

## Installed Location

- **Path:** `C:\Users\sony\OneDrive\Desktop\llm-council`
- **Virtual Environment:** `C:\Users\sony\OneDrive\Desktop\llm-council\.venv`
- **Config:** `C:\Users\sony\OneDrive\Desktop\llm-council\backend\config.py`
- **API Key:** Configured in `C:\Users\sony\OneDrive\Desktop\llm-council\.env` (`OPENROUTER_API_KEY`)

## How to Use from Antigravity / Any Project

### 1. Launch the Web Interface
Double-click `start.bat` in `C:\Users\sony\OneDrive\Desktop\llm-council` or run in PowerShell:
```powershell
& "C:\Users\sony\OneDrive\Desktop\llm-council\start.bat"
```
This boots:
- **Backend API:** `http://localhost:8001`
- **Frontend App:** `http://localhost:5173`

### 2. Run Direct Council Deliberation via CLI
You can run questions or architecture debates directly from the terminal or subagents:
```powershell
& "C:\Users\sony\OneDrive\Desktop\llm-council\.venv\Scripts\python.exe" "C:\Users\sony\OneDrive\Desktop\llm-council\cli.py" "Your question or design decision here"
```

### 3. Query Council via REST API
When the backend is running (`http://localhost:8001`):
- `POST http://localhost:8001/api/conversations` (Create session)
- `POST http://localhost:8001/api/conversations/{id}/message` (Submit query and get Stage 1, Stage 2 rankings, and Stage 3 synthesis)
