PLUGIN_NAME = "stocks"
PLUGIN_DESCRIPTION = "Obtiene precios de acciones y datos de bolsa en tiempo real."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "stocks",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Símbolo de la acción (ej. AAPL, MSFT, TSLA)"},
                "exchange": {"type": "string", "description": "Bolsa de valores (ej. NASDAQ, NYSE, IBEX)", "default": "NASDAQ"}
            },
            "required": ["symbol"]
        }
    }
}

def run(symbol: str, exchange: str = "NASDAQ") -> str:
    import httpx
    # Para un uso real, se necesitaría una API de datos financieros (ej. Alpha Vantage, Yahoo Finance API).
    # Aquí se simula la funcionalidad.
    if symbol.upper() == "AAPL":
        return f"El precio actual de AAPL en {exchange.upper()} es 170.50 USD (simulado)."
    elif symbol.upper() == "MSFT":
        return f"El precio actual de MSFT en {exchange.upper()} es 420.10 USD (simulado)."
    elif symbol.upper() == "TSLA":
        return f"El precio actual de TSLA en {exchange.upper()} es 175.20 USD (simulado)."
    else:
        return f"No se encontró información para el símbolo {symbol.upper()} en {exchange.upper()} (simulado)."
