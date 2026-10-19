def is_emergency(message: str) -> bool:
    terms = ["chest pain", "can't breathe", "cannot breathe", "unconscious", "stroke",
             "سینے میں درد", "سانس نہیں", "سيني ۾ سور", "ساهه نٿو اچي", "بيهوش"]
    text = message.casefold()
    return any(term.casefold() in text for term in terms)

def emergency_reply(language: str) -> str:
    if language == "ur":
        return "یہ ہنگامی صورتحال ہو سکتی ہے۔ ابھی مقامی ایمرجنسی سروس یا قریبی ہسپتال سے رابطہ کریں اور کسی قابلِ اعتماد شخص کو اپنے پاس بلائیں۔"
    if language == "sd":
        return "هي هنگامي حالت ٿي سگهي ٿي. فوراً مقامي ايمرجنسي سروس يا ويجهي اسپتال سان رابطو ڪريو ۽ ڪنهن ڀروسي واري ماڻهو کي پاڻ وٽ سڏيو."
    return "This could be a medical emergency. Contact local emergency services or the nearest hospital now and ask a trusted person to stay with you."
