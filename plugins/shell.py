PLUGIN_NAME = "shell"
PLUGIN_DESCRIPTION = "Ejecuta comandos de shell de forma segura en el sistema."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "shell",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "El comando de shell a ejecutar"}
            },
            "required": ["command"]
        }
    }
}

def run(command: str) -> str:
    import subprocess
    try:
        # Advertencia: Ejecutar comandos de shell directamente puede ser un riesgo de seguridad.
        # En un entorno de producción, se deberían implementar estrictas validaciones y listas blancas.
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return f"Salida:\n{result.stdout}\nErrores:\n{result.stderr}"
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e.stderr}"
    except Exception as e:
        return f"Error inesperado al ejecutar el comando de shell: {e}"
