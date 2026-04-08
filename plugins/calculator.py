PLUGIN_NAME = "calculator"
PLUGIN_DESCRIPTION = "Realiza operaciones aritméticas básicas como suma, resta, multiplicación y división."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "description": "La operación a realizar (sum, subtract, multiply, divide)",
                    "enum": ["sum", "subtract", "multiply", "divide"]
                },
                "num1": {
                    "type": "number",
                    "description": "El primer número"
                },
                "num2": {
                    "type": "number",
                    "description": "El segundo número"
                }
            },
            "required": ["operation", "num1", "num2"]
        }
    }
}

def run(operation: str, num1: float, num2: float) -> str:
    if operation == "sum":
        return str(num1 + num2)
    elif operation == "subtract":
        return str(num1 - num2)
    elif operation == "multiply":
        return str(num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            return "Error: División por cero"
        return str(num1 / num2)
    else:
        return "Error: Operación no soportada"
