PLUGIN_NAME = "spotify"
PLUGIN_DESCRIPTION = "Controla la reproducción de Spotify y busca contenido."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "spotify",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar en Spotify (play, pause, next, previous, search, current_song, playlists)",
                    "enum": ["play", "pause", "next", "previous", "search", "current_song", "playlists"]
                },
                "query": {
                    "type": "string",
                    "description": "Término de búsqueda para canciones o artistas (requerido para 'search')"
                },
                "type": {
                    "type": "string",
                    "description": "Tipo de búsqueda (track, artist, album, playlist) (requerido para 'search')",
                    "enum": ["track", "artist", "album", "playlist"]
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, query: str = None, type: str = None) -> str:
    # En un entorno real, aquí se integraría con la API de Spotify (spotipy).
    # Se necesitaría autenticación OAuth2.
    if action == "play":
        return "Reproduciendo Spotify... (simulado)"
    elif action == "pause":
        return "Spotify en pausa... (simulado)"
    elif action == "next":
        return "Siguiente canción... (simulado)"
    elif action == "previous":
        return "Canción anterior... (simulado)"
    elif action == "search":
        if not query or not type:
            return "Error: 'query' y 'type' son requeridos para la acción 'search'."
        return f"Buscando {type} '{query}' en Spotify... (simulado)"
    elif action == "current_song":
        return "Canción actual: 'Simulated Song' by 'Simulated Artist' (simulado)"
    elif action == "playlists":
        return "Listando playlists... (simulado)"
    else:
        return "Acción de Spotify no reconocida."
