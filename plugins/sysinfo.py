PLUGIN_NAME = "sysinfo"
PLUGIN_DESCRIPTION = "Obtiene información básica del sistema operativo y hardware."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "sysinfo",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

def run() -> str:
    import platform
    import os

    info = {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "cpu_cores": os.cpu_count()
    }
    return str(info)
