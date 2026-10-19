from .config import AI_PROVIDER, OPENAI_API_KEY, OPENAI_MODEL
from .safety import is_emergency, emergency_reply

SYSTEM_PROMPT = (
    "You are Suharo AI, a cautious health-information assistant for older adults. Ada and Adi are the friendly virtual companion characters. "
    "Give general education only. Never diagnose, prescribe, or change medication doses. "
    "Encourage qualified clinicians for personal decisions. For possible emergencies, advise immediate local emergency care. "
    "Do not claim to contact doctors or know every government scheme. Use plain respectful language."
)

def reply(message: str, language: str) -> str:
    if is_emergency(message):
        return emergency_reply(language)
    if AI_PROVIDER == "openai" and OPENAI_API_KEY:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=OPENAI_API_KEY)
            language_name = {"sd": "Sindhi", "ur": "Urdu", "en": "English"}[language]
            result = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT + f" Reply in {language_name}."},
                    {"role": "user", "content": message[:4000]},
                ],
                temperature=0.2,
            )
            return (result.choices[0].message.content or "").strip() or fallback(language)
        except Exception:
            return fallback(language)
    return fallback(language)

def fallback(language: str) -> str:
    if language == "ur":
        return "میں عمومی صحت کی معلومات دے سکتا ہوں، لیکن تشخیص یا دوا تجویز نہیں کر سکتا۔ علامات شدید ہوں یا بڑھ رہی ہوں تو ڈاکٹر سے رابطہ کریں۔"
    if language == "sd":
        return "مان عام صحت بابت ڄاڻ ڏئي سگهان ٿو، پر تشخيص يا دوا تجويز نٿو ڪري سگهان. تڪليف شديد هجي ته ڊاڪٽر سان رابطو ڪريو."
    return "I can share general health information, but I cannot diagnose or prescribe medicine. If symptoms are severe, new, or worsening, contact a qualified clinician."
