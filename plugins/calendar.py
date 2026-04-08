PLUGIN_NAME = "calendar"
PLUGIN_DESCRIPTION = "Gestiona fechas, horas, recordatorios y eventos."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "calendar",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Acción a realizar (current_datetime, set_reminder, add_event, list_events)",
                    "enum": ["current_datetime", "set_reminder", "add_event", "list_events"]
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Fecha y hora para el recordatorio o evento (ej. \"2026-04-08 10:30\")"
                },
                "description": {
                    "type": "string",
                    "description": "Descripción del recordatorio o evento"
                }
            },
            "required": ["action"]
        }
    }
}

# Simulación de almacenamiento de eventos y recordatorios
events = []

def run(action: str, datetime_str: str = None, description: str = None) -> str:
    import datetime

    if action == "current_datetime":
        return f"Fecha y hora actuales: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    elif action == "set_reminder":
        if not datetime_str or not description:
            return "Error: Se requiere fecha/hora y descripción para establecer un recordatorio."
        try:
            dt_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            events.append({"type": "reminder", "datetime": dt_obj, "description": description})
            return f"Recordatorio establecido para {datetime_str}: {description}"
        except ValueError:
            return "Error: Formato de fecha y hora inválido. Use YYYY-MM-DD HH:MM."
    elif action == "add_event":
        if not datetime_str or not description:
            return "Error: Se requiere fecha/hora y descripción para añadir un evento."
        try:
            dt_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            events.append({"type": "event", "datetime": dt_obj, "description": description})
            return f"Evento añadido para {datetime_str}: {description}"
        except ValueError:
            return "Error: Formato de fecha y hora inválido. Use YYYY-MM-DD HH:MM."
    elif action == "list_events":
        if not events:
            return "No hay recordatorios ni eventos programados."
        output = "Recordatorios y Eventos:\n"
        for item in sorted(events, key=lambda x: x["datetime"]):
            output += f"[{item["type"].capitalize()}] {item["datetime"].strftime("%Y-%m-%d %H:%M")}: {item["description"]}\n"
        return output
    else:
        return "Acción de calendario no reconocida."
