PLUGIN_NAME = "todo"
PLUGIN_DESCRIPTION = "Gestiona una lista de tareas persistente (añadir, listar, completar, eliminar)."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "todo",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (add, list, complete, delete)",
                    "enum": ["add", "list", "complete", "delete"]
                },
                "task": {
                    "type": "string",
                    "description": "Descripción de la tarea (requerido para add)"
                },
                "task_id": {
                    "type": "integer",
                    "description": "ID de la tarea (requerido para complete, delete)"
                }
            },
            "required": ["action"]
        }
    }
}

# Simulación de una base de datos de tareas
todo_list = []
next_id = 1

def run(action: str, task: str = None, task_id: int = None) -> str:
    global todo_list, next_id

    if action == "add":
        if not task:
            return "Error: La descripción de la tarea es requerida para la acción 'add'."
        todo_list.append({"id": next_id, "task": task, "completed": False})
        next_id += 1
        return f"Tarea '{task}' añadida con ID {next_id - 1}."
    elif action == "list":
        if not todo_list:
            return "No hay tareas en la lista."
        output = "Lista de Tareas:\n"
        for item in todo_list:
            status = "[X]" if item["completed"] else "[ ]"
            output += f"{status} {item['id']}: {item['task']}\n"
        return output
    elif action == "complete":
        if task_id is None:
            return "Error: El ID de la tarea es requerido para la acción 'complete'."
        for item in todo_list:
            if item["id"] == task_id:
                item["completed"] = True
                return f"Tarea {task_id} marcada como completada."
        return f"Error: No se encontró la tarea con ID {task_id}."
    elif action == "delete":
        if task_id is None:
            return "Error: El ID de la tarea es requerido para la acción 'delete'."
        original_len = len(todo_list)
        todo_list = [item for item in todo_list if item["id"] != task_id]
        if len(todo_list) < original_len:
            return f"Tarea {task_id} eliminada."
        return f"Error: No se encontró la tarea con ID {task_id}."
    else:
        return "Acción de lista de tareas no reconocida."
