# Suharo AI — Your Caring AI Health Companion

**Sindhi tagline:** توهان جي صحت، توهان جو سهارو  
**Purpose:** Friendly, multilingual general health information for older adults and families. Ada and Adi remain the virtual companion characters within the Suharo AI brand.

Suharo AI is an early-stage demonstration built with a lightweight web frontend and a FastAPI backend. It includes a responsive dashboard, original companion illustrations, multilingual chat scaffolding, browser-dependent voice controls, demo reminders, basic emergency-keyword routing, and automated tests. The project includes a coherent teal/sage/cream brand palette, primary logo, app icon, favicon, and branded interface.

> **Important:** This is a prototype, not a medical device or production-ready healthcare system. Do not enter real patient data. It does not diagnose, prescribe, contact a doctor, send actual reminder notifications, or provide a verified emergency service.

## Run on Windows

1. Install Python 3.10 or newer and extract this ZIP.
2. Double-click `run_windows.bat`, or open PowerShell in the project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload
```

3. Open `http://127.0.0.1:8000`.
4. Run tests with `test_windows.bat` or `.\.venv\Scripts\python.exe -m pytest -q`.

## Brand assets

- `frontend/assets/suharo-ai-logo.png` — full logo for documents and larger brand placements
- `frontend/assets/suharo-ai-icon.png` — compact symbol for the header and app identity
- `frontend/assets/favicon.png` — browser tab icon
- `frontend/assets/ada-avatar.svg` and `frontend/assets/adi-avatar.svg` — virtual companion illustrations

The visual identity uses deep teal, sage green, soft mint, and warm cream to feel calm, accessible, and trustworthy.

## Voice and AI configuration

The default `AI_PROVIDER=demo` keeps the app runnable without paid services or credentials; demo responses are placeholders. Optional hosted text and text-to-speech features can be configured server-side. Never place API keys in frontend JavaScript or commit `.env` files.

Sindhi speech quality depends on the selected provider, browser, and operating system. The integration does not guarantee native-quality Sindhi pronunciation. The avatars are 2D SVG illustrations, not rigged 3D characters, and the speaking animation is not synchronized lip movement.

## Before any real-world use

Add and independently review authentication, role-based access, HTTPS, rate limiting, informed consent, encryption, audit logging, retention/deletion controls, clinician-reviewed content, tested Sindhi speech, and a verified emergency escalation process. Emergency keyword detection is incomplete and must never be relied upon as the only safeguard. Obtain clinical, security, and privacy review before any public healthcare deployment.

## Main folders

- `frontend/` — interface, styling, browser voice controls, logo and avatar assets
- `backend/` — FastAPI routes, assistant logic, voice endpoint, safety routing, SQLite demo reminders
- `tests/` — API tests
- `docs/ARCHITECTURE.md` — architecture notes and production recommendations
- `.env.example` — optional server configuration template
- `run_windows.bat` — install and launch helper
- `test_windows.bat` — test helper
