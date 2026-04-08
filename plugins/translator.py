PLUGIN_NAME = "translator"
PLUGIN_DESCRIPTION = "Traduce texto entre diferentes idiomas, detectando el idioma de origen automáticamente."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "translator",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "El texto a traducir"},
                "target_language": {"type": "string", "description": "El idioma al que se desea traducir (código ISO 639-1, ej. en, es, fr)"}
            },
            "required": ["text", "target_language"]
        }
    }
}

def run(text: str, target_language: str) -> str:
    try:
        from deep_translator import GoogleTranslator
        # La detección automática de idioma se maneja internamente por GoogleTranslator si no se especifica source
        translated_text = GoogleTranslator(target=target_language).translate(text)
        return f"Texto original: 
{text}
Traducido a {target_language}: 
{translated_text}"
    except ImportError:
        return "Error: La librería 'deep_translator' no está instalada. Por favor, instálala con 'pip install deep-translator'."
    except Exception as e:
        return f"Error al traducir: {e}"
