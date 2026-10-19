from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator
from .database import init_db, all_reminders, create_reminder, remove_reminder
from .assistant import reply
from .config import AI_PROVIDER, OPENAI_API_KEY, OPENAI_TTS_MODEL, OPENAI_TTS_VOICE

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Suharo AI Prototype API", version="0.1.0", lifespan=lifespan)

class ChatInput(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    language: str = "en"
    @field_validator("language")
    @classmethod
    def language_allowed(cls, value):
        if value not in {"sd", "ur", "en"}:
            raise ValueError("language must be sd, ur, or en")
        return value

class ReminderInput(BaseModel):
    label: str = Field(min_length=1, max_length=120)
    time: str = Field(pattern=r"^(?:[01]\d|2[0-3]):[0-5]\d$")

class VoiceInput(BaseModel):
    text: str = Field(min_length=1, max_length=1800)
    language: str = "sd"
    @field_validator("language")
    @classmethod
    def voice_language_allowed(cls, value):
        if value not in {"sd", "ur", "en"}:
            raise ValueError("language must be sd, ur, or en")
        return value

@app.post("/api/voice")
def voice(data: VoiceInput):
    """Optional server-side TTS. Requires OPENAI_API_KEY and the optional openai package."""
    if AI_PROVIDER != "openai" or not OPENAI_API_KEY:
        raise HTTPException(status_code=503, detail="Hosted voice is not configured. Add OPENAI_API_KEY and set AI_PROVIDER=openai, or use browser voice if available.")
    try:
        from openai import OpenAI
        language_name = {"sd": "Sindhi", "ur": "Urdu", "en": "English"}[data.language]
        client = OpenAI(api_key=OPENAI_API_KEY)
        audio = client.audio.speech.create(
            model=OPENAI_TTS_MODEL,
            voice=OPENAI_TTS_VOICE,
            input=data.text.strip(),
            instructions=f"Speak clearly and warmly in {language_name}, at a gentle pace for older listeners. Do not translate or add words."
        )
        return Response(content=audio.content, media_type="audio/mpeg", headers={"Cache-Control": "no-store"})
    except ImportError:
        raise HTTPException(status_code=503, detail="Install the optional openai package to enable hosted voice.")
    except Exception:
        raise HTTPException(status_code=502, detail="Voice generation failed. Check provider access, model availability, and API billing.")

@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "prototype"}

@app.post("/api/chat")
def chat(data: ChatInput):
    return {"reply": reply(data.message.strip(), data.language),
            "disclaimer": "General information only; not diagnosis or prescription."}

@app.get("/api/reminders")
def reminders():
    return {"items": all_reminders(), "demo": True}

@app.post("/api/reminders", status_code=201)
def add(data: ReminderInput):
    label = data.label.strip()
    if not label:
        raise HTTPException(422, "Label cannot be blank")
    return create_reminder(label, data.time)

@app.delete("/api/reminders/{item_id}")
def delete(item_id: int):
    if not remove_reminder(item_id):
        raise HTTPException(404, "Reminder not found")
    return {"deleted": True}

ROOT = Path(__file__).resolve().parent.parent
app.mount("/", StaticFiles(directory=str(ROOT / "frontend"), html=True), name="frontend")
