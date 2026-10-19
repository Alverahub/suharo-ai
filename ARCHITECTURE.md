# Architecture and production boundaries

## Prototype flow
Browser UI (SVG cartoon characters, multilingual chat and voice controls) -> FastAPI -> request validation -> basic emergency keyword routing -> demo responder or optional hosted AI -> SQLite demo reminders. Hosted text-to-speech is exposed through a server-side endpoint so API credentials are not sent to the browser.

## Included
- Local cartoon SVG assets for Ada and Adi.
- Automatic/manual voice playback attempts, optional hosted TTS, and browser speech recognition where available.
- Language input validation and a simple emergency response route.
- SQLite reminders intended for demonstration only.
- Basic API tests.

## Not included / not production-ready
- True 3D rigged avatars or phoneme/viseme-driven lip-sync.
- Guaranteed native-quality Sindhi TTS or Sindhi ASR; language support must be tested with native speakers.
- Authentication, patient accounts, family sharing, clinician escalation, actual reminder notifications, or verified benefit information.
- Complete clinical safety coverage; keyword-based emergency detection can miss urgent symptoms.

## Production path
Use licensed/custom rigged 3D characters with facial blendshapes and viseme support; select a tested Sindhi ASR/TTS provider or commission consented native-speaker recordings; add clinician-reviewed knowledge content; implement authentication, role-based authorization, HTTPS, encryption, consent, audit logs, rate limiting, retention policies, monitoring, verified emergency workflows, and independent clinical/security/privacy review.
