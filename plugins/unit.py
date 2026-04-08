PLUGIN_NAME = "unit"
PLUGIN_DESCRIPTION = "Convierte unidades de peso, longitud, temperatura, volumen, etc."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "unit",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "value": {"type": "number", "description": "El valor a convertir"},
                "from_unit": {"type": "string", "description": "La unidad de origen (ej. meters, feet, celsius, fahrenheit, kg, lbs)"},
                "to_unit": {"type": "string", "description": "La unidad de destino (ej. meters, feet, celsius, fahrenheit, kg, lbs)"}
            },
            "required": ["value", "from_unit", "to_unit"]
        }
    }
}

def run(value: float, from_unit: str, to_unit: str) -> str:
    # Simplificación para el ejemplo. Una implementación real usaría un diccionario de factores de conversión
    # o una librería dedicada como `pint`.
    conversions = {
        "meters_to_feet": 3.28084,
        "feet_to_meters": 0.3048,
        "celsius_to_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9,
        "kg_to_lbs": 2.20462,
        "lbs_to_kg": 0.453592
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return f"{value} {from_unit} es igual a {value} {to_unit}"

    if from_unit == "meters" and to_unit == "feet":
        converted_value = value * conversions["meters_to_feet"]
    elif from_unit == "feet" and to_unit == "meters":
        converted_value = value * conversions["feet_to_meters"]
    elif from_unit == "celsius" and to_unit == "fahrenheit":
        converted_value = conversions["celsius_to_fahrenheit"](value)
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        converted_value = conversions["fahrenheit_to_celsius"](value)
    elif from_unit == "kg" and to_unit == "lbs":
        converted_value = value * conversions["kg_to_lbs"]
    elif from_unit == "lbs" and to_unit == "kg":
        converted_value = value * conversions["lbs_to_kg"]
    else:
        return f"Error: Conversión de {from_unit} a {to_unit} no soportada o unidades inválidas."

    return f"{value} {from_unit} es igual a {converted_value:.2f} {to_unit}"
