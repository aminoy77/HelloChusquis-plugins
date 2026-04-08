PLUGIN_NAME = "ip"
PLUGIN_DESCRIPTION = "Obtiene información de la IP pública y geolocalización."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "ip",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

def run() -> str:
    import httpx
    try:
        response = httpx.get("https://ipinfo.io/json", timeout=10)
        response.raise_for_status()
        data = response.json()
        output = f"IP Pública: {data.get("ip")}\n"
        output += f"Ciudad: {data.get("city")}\n"
        output += f"Región: {data.get("region")}\n"
        output += f"País: {data.get("country")}\n"
        output += f"Coordenadas: {data.get("loc")}\n"
        output += f"Organización: {data.get("org")}"
        return output
    except httpx.RequestError as e:
        return f"Error de conexión al obtener información de IP: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al obtener información de IP: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al obtener información de IP: {e}"
