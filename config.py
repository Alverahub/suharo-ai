import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_PATH = os.getenv("DATABASE_PATH", "./ada_adi_demo.db")
AI_PROVIDER = os.getenv("AI_PROVIDER", "demo").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_TTS_MODEL = os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")
OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE", "shimmer")
