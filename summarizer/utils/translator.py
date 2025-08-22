from googletrans import Translator

# Supported languages dictionary
SUPPORTED_LANGUAGES = {
    'hindi': 'hi',
    'tamil': 'ta',
    'bengali': 'bn',
    'gujarati': 'gu',
    'telugu': 'te',
    'punjabi': 'pa',
    'kannada': 'kn',
    'malayalam': 'ml',
    'marathi': 'mr',
    'urdu': 'ur',
}

# ✅ Function to load translator based on language
def load_translator(target_language):
    lang_code = SUPPORTED_LANGUAGES.get(target_language.lower())
    if not lang_code:
        raise ValueError(f"Unsupported language: {target_language}")

    translator = Translator()

    def translate_fn(text):
        result = translator.translate(text, dest=lang_code)
        return result.text

    return translate_fn

def translate_text(translate_fn, text, chunk_size=2000):
    """
    Translate the text in smaller chunks to avoid Google Translate limits.
    """
    translated_chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        translated_chunk = translate_fn(chunk)
        translated_chunks.append(translated_chunk)
    return " ".join(translated_chunks)
