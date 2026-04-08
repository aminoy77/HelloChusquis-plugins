PLUGIN_NAME = "wikipedia"
PLUGIN_DESCRIPTION = "Busca información en Wikipedia y devuelve un resumen."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "wikipedia",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "El término de búsqueda para Wikipedia"}
            },
            "required": ["query"]
        }
    }
}

def run(query: str) -> str:
    try:
        import wikipedia
        wikipedia.set_lang("es")
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return f"Error al buscar en Wikipedia: {e}"
