from data.texts import es, en, cat

LANGUAGES = {
    "es": es,
    "cat": cat,
    "en": en
}

def get_text(lang_code, key):
    """Retorna el text segons idioma i clau"""
    
    texts = LANGUAGES.get(lang_code, es)  # default castellà
    return getattr(texts, key)