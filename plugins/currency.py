PLUGIN_NAME = "currency"
PLUGIN_DESCRIPTION = "Convierte una cantidad de una moneda a otra utilizando tasas de cambio actuales."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "currency",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number", "description": "La cantidad a convertir"},
                "from_currency": {"type": "string", "description": "La moneda de origen (código ISO 4217, ej. USD)"},
                "to_currency": {"type": "string", "description": "La moneda de destino (código ISO 4217, ej. EUR)"}
            },
            "required": ["amount", "from_currency", "to_currency"]
        }
    }
}

def run(amount: float, from_currency: str, to_currency: str) -> str:
    import httpx
    # Puedes usar una API gratuita como ExchangeRate-API o similar.
    # Para este ejemplo, usaremos una tasa de cambio fija o un mock.
    # En un entorno real, necesitarías una clave API y manejar errores de la API.
    
    # Ejemplo con tasas de cambio fijas (solo para demostración)
    exchange_rates = {
        "USD": {"EUR": 0.92, "GBP": 0.79, "JPY": 155.0},
        "EUR": {"USD": 1.09, "GBP": 0.86, "JPY": 168.0},
        "GBP": {"USD": 1.27, "EUR": 1.16, "JPY": 195.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051}
    }

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return f"Error: No se encontró la tasa de cambio para {from_currency} a {to_currency}."

    converted_amount = amount * exchange_rates[from_currency][to_currency]
    return f"{amount} {from_currency} es igual a {converted_amount:.2f} {to_currency}"
