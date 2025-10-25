"""
Configuration file for Urdu Voice Assistant
Handles all application settings and paths
"""

import os
from pathlib import Path

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

# API Settings
API_VERSION = "1.0.0"
API_PREFIX = "/api/v1"
PROJECT_NAME = "Urdu Voice Assistant"
PROJECT_DESCRIPTION = "Production-ready Urdu Voice Assistant for Pakistani users"

# CORS Settings
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",  # Vite default port
    "http://127.0.0.1:5173"
]

# Audio Settings
AUDIO_OUTPUT_DIR = BASE_DIR / "audio_outputs"
MAX_AUDIO_FILES = 100
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "high"  # Options: low, medium, high

# Speech Settings
DEFAULT_LANGUAGE = "ur"  # Urdu
FALLBACK_LANGUAGE = "en"  # English
SPEECH_RATE = 1.0  # Normal speed
SUPPORTED_LANGUAGES = ["ur", "en", "mixed"]

# Logging Configuration
LOG_DIR = BASE_DIR / "logs"
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Data Files Paths
DATA_DIR = BASE_DIR / "data"
RESPONSES_FILE = DATA_DIR / "responses.json"
JOKES_FILE = DATA_DIR / "jokes.json"
COMMANDS_FILE = DATA_DIR / "commands.json"
PATTERNS_FILE = DATA_DIR / "patterns.json"

# Server Settings
HOST = "0.0.0.0"
PORT = 8000
RELOAD = True  # Set to False in production
SERVER_HOST = HOST  # Backward compatibility
SERVER_PORT = PORT  # Backward compatibility
SERVER_RELOAD = RELOAD  # Backward compatibility

# Intent Detection Settings
MIN_CONFIDENCE_THRESHOLD = 0.5
UNKNOWN_INTENT_THRESHOLD = 0.3

# Create required directories if they don't exist
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Environment variables (can be overridden by .env file)
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
MAX_REQUEST_SIZE = int(os.getenv("MAX_REQUEST_SIZE", "5242880"))  # 5MB default

print(f"✅ Configuration loaded successfully!")
print(f"📁 Base Directory: {BASE_DIR}")
print(f"🎤 Audio Output: {AUDIO_OUTPUT_DIR}")
print(f"📝 Logs Directory: {LOG_DIR}")
