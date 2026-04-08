PLUGIN_NAME = "news"
PLUGIN_DESCRIPTION = "Obtiene las últimas noticias de una categoría o palabra clave específica."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "news",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Categoría de noticias (ej. technology, sports, business)", "enum": ["technology", "sports", "business", "general"]},
                "keyword": {"type": "string", "description": "Palabra clave para buscar en las noticias"}
            },
            "required": ["category"]
        }
    }
}

def run(category: str, keyword: str = None) -> str:
    # En un entorno real, esto haría una llamada a una API de noticias (ej. NewsAPI, GNews API)
    # Para este ejemplo, simularemos algunas noticias.
    if category == "technology":
        if keyword and "AI" in keyword:
            return "Noticia: El avance de la IA genera debate ético. Noticia: Nuevos chips de IA prometen mayor rendimiento."
        return "Noticia: Apple lanza su nuevo iPhone. Noticia: Google presenta innovaciones en la nube."
    elif category == "sports":
        return "Noticia: El equipo local gana el campeonato. Noticia: Récord mundial en atletismo."
    elif category == "business":
        return "Noticia: La bolsa de valores cierra al alza. Noticia: Fusión de grandes empresas tecnológicas."
    else:
        return "Noticia: Titular general 1. Noticia: Titular general 2."
