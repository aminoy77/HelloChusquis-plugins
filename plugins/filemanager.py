PLUGIN_NAME = "filemanager"
PLUGIN_DESCRIPTION = "Gestiona archivos y directorios en el sistema de archivos (leer, escribir, listar, crear, borrar, renombrar)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "filemanager",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (read, write, list, create_dir, delete, rename)",
                    "enum": ["read", "write", "list", "create_dir", "delete", "rename"]
                },
                "path": {
                    "type": "string",
                    "description": "Ruta del archivo o directorio"
                },
                "content": {
                    "type": "string",
                    "description": "Contenido a escribir en el archivo (requerido para 'write')"
                },
                "new_path": {
                    "type": "string",
                    "description": "Nueva ruta o nombre para renombrar (requerido para 'rename')"
                }
            },
            "required": ["action", "path"]
        }
    }
}

def run(action: str, path: str, content: str = None, new_path: str = None) -> str:
    import os
    import shutil

    try:
        if action == "read":
            if not os.path.exists(path) or not os.path.isfile(path):
                return f"Error: El archivo {path} no existe o no es un archivo."
            with open(path, 'r') as f:
                return f.read()
        elif action == "write":
            if not content:
                return "Error: El contenido es requerido para la acción 'write'."
            with open(path, 'w') as f:
                f.write(content)
            return f"Archivo {path} escrito exitosamente."
        elif action == "list":
            if not os.path.exists(path) or not os.path.isdir(path):
                return f"Error: El directorio {path} no existe o no es un directorio."
            return str(os.listdir(path))
        elif action == "create_dir":
            os.makedirs(path, exist_ok=True)
            return f"Directorio {path} creado exitosamente."
        elif action == "delete":
            if os.path.isfile(path):
                os.remove(path)
                return f"Archivo {path} eliminado exitosamente."
            elif os.path.isdir(path):
                shutil.rmtree(path)
                return f"Directorio {path} y su contenido eliminados exitosamente."
            else:
                return f"Error: {path} no existe o no es un archivo/directorio válido."
        elif action == "rename":
            if not new_path:
                return "Error: La nueva ruta o nombre es requerido para la acción 'rename'."
            if not os.path.exists(path):
                return f"Error: {path} no existe."
            os.rename(path, new_path)
            return f"Renombrado {path} a {new_path} exitosamente."
        else:
            return "Acción de gestor de archivos no reconocida."
    except Exception as e:
        return f"Error en el gestor de archivos: {e}"
