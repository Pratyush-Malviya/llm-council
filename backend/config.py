"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
# Reads from COUNCIL_MODELS in .env if provided (comma-separated), otherwise uses active top-tier models
_env_council = os.getenv("COUNCIL_MODELS")
if _env_council:
    COUNCIL_MODELS = [m.strip() for m in _env_council.split(",") if m.strip()]
else:
    COUNCIL_MODELS = [
        "anthropic/claude-3.5-sonnet",
        "openai/gpt-4o",
        "google/gemini-2.0-flash-001",
        "meta-llama/llama-3.3-70b-instruct",
    ]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = os.getenv("CHAIRMAN_MODEL", "anthropic/claude-3.5-sonnet")

# OpenRouter API endpoint
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL", "https://openrouter.ai/api/v1/chat/completions")

# Data directory for conversation storage
DATA_DIR = "data/conversations"
