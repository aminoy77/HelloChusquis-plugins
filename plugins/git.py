PLUGIN_NAME = "git"
PLUGIN_DESCRIPTION = "Asistente para operaciones básicas de Git (status, add, commit, push, pull, branch, log)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "git",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción de Git a realizar (status, add, commit, push, pull, branch, log)",
                    "enum": ["status", "add", "commit", "push", "pull", "branch", "log"]
                },
                "message": {
                    "type": "string",
                    "description": "Mensaje para el commit (requerido para 'commit')"
                },
                "files": {
                    "type": "string",
                    "description": "Archivos a añadir (ej. "." para todos, o "file1 file2") (requerido para 'add')"
                },
                "branch_name": {
                    "type": "string",
                    "description": "Nombre de la rama (requerido para 'branch' si se crea una nueva)"
                }
            },
            "required": ["action"]
        }
    }
}

def run(action: str, message: str = None, files: str = None, branch_name: str = None) -> str:
    import subprocess

    try:
        if action == "status":
            result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
            return result.stdout
        elif action == "add":
            if not files:
                return "Error: Se requieren archivos para la acción 'add'."
            result = subprocess.run(["git", "add"] + files.split(), capture_output=True, text=True, check=True)
            return result.stdout
        elif action == "commit":
            if not message:
                return "Error: Se requiere un mensaje para la acción 'commit'."
            result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True, check=True)
            return result.stdout
        elif action == "push":
            result = subprocess.run(["git", "push"], capture_output=True, text=True, check=True)
            return result.stdout
        elif action == "pull":
            result = subprocess.run(["git", "pull"], capture_output=True, text=True, check=True)
            return result.stdout
        elif action == "branch":
            if branch_name:
                result = subprocess.run(["git", "checkout", "-b", branch_name], capture_output=True, text=True, check=True)
                return f"Rama {branch_name} creada y cambiada exitosamente.\n" + result.stdout
            else:
                result = subprocess.run(["git", "branch"], capture_output=True, text=True, check=True)
                return result.stdout
        elif action == "log":
            result = subprocess.run(["git", "log", "--oneline"], capture_output=True, text=True, check=True)
            return result.stdout
        else:
            return "Acción de Git no reconocida."
    except FileNotFoundError:
        return "Error: Git no está instalado o no se encuentra en el PATH."
    except subprocess.CalledProcessError as e:
        return f"Error en la ejecución de Git: {e.stderr}"
    except Exception as e:
        return f"Error inesperado en el plugin Git: {e}"
