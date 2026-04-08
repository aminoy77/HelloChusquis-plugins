PLUGIN_NAME = "qr"
PLUGIN_DESCRIPTION = "Genera códigos QR a partir de texto o URLs."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "qr",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "El texto o URL para codificar en el QR"},
                "filename": {"type": "string", "description": "Nombre del archivo de imagen QR a guardar (ej. my_qr.png)", "default": "qrcode.png"}
            },
            "required": ["data"]
        }
    }
}

def run(data: str, filename: str = "qrcode.png") -> str:
    try:
        import qrcode
        img = qrcode.make(data)
        img.save(filename)
        return f"Código QR generado y guardado como {filename}"
    except ImportError:
        return "Error: La librería 'qrcode' no está instalada. Por favor, instálala con 'pip install qrcode'."
    except Exception as e:
        return f"Error al generar el código QR: {e}"
