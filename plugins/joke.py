PLUGIN_NAME = "joke"
PLUGIN_DESCRIPTION = "Cuenta chistes aleatorios en español."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "joke",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

def run() -> str:
    jokes = [
        "¿Qué le dice un semáforo a otro semáforo? No me mires que me estoy cambiando.",
        "¿Cuál es el colmo de un jardinero? Que siempre lo dejen plantado.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Qué le dice una impresora a otra? ¿Esa hoja es tuya o es impresión mía?",
        "¿Qué hace una vaca en un tejado? ¡Vaca-ciones!"
    ]
    import random
    return random.choice(jokes)
