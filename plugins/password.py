PLUGIN_NAME = "password"
PLUGIN_DESCRIPTION = "Genera contraseñas seguras y personalizables."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "password",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "length": {"type": "integer", "description": "Longitud de la contraseña", "default": 12},
                "include_uppercase": {"type": "boolean", "description": "Incluir letras mayúsculas", "default": True},
                "include_lowercase": {"type": "boolean", "description": "Incluir letras minúsculas", "default": True},
                "include_digits": {"type": "boolean", "description": "Incluir dígitos", "default": True},
                "include_symbols": {"type": "boolean", "description": "Incluir símbolos", "default": True}
            },
            "required": []
        }
    }
}

def run(length: int = 12, include_uppercase: bool = True, include_lowercase: bool = True, include_digits: bool = True, include_symbols: bool = True) -> str:
    import random
    import string

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: Debe seleccionar al menos un tipo de carácter para generar la contraseña."

    password = ".join(random.choice(characters) for i in range(length))"
    return f"Contraseña generada: {password}"
