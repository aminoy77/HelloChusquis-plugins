PLUGIN_NAME = "youtube"
PLUGIN_DESCRIPTION = "Busca videos en YouTube, obtiene información y descarga audio o enlaces."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "youtube",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (search, info, download_audio, get_link)",
                    "enum": ["search", "info", "download_audio", "get_link"]
                },
                "query": {
                    "type": "string",
                    "description": "Término de búsqueda o URL del video (requerido para todas las acciones)"
                }
            },
            "required": ["action", "query"]
        }
    }
}

def run(action: str, query: str) -> str:
    # Para un uso real, se necesitaría una API de YouTube o librerías como `yt-dlp`.
    # Aquí se simula la funcionalidad.
    if action == "search":
        return f"Buscando videos de YouTube para \'{query}\'... (simulado)"
    elif action == "info":
        return f"Obteniendo información para el video/URL \'{query}\'... (simulado)"
    elif action == "download_audio":
        return f"Descargando audio del video/URL \'{query}\'... (simulado)"
    elif action == "get_link":
        return f"Obteniendo enlace del video/URL \'{query}\'... (simulado)"
    else:
        return "Acción de YouTube no reconocida."
