PLUGIN_NAME = "crypto"
PLUGIN_DESCRIPTION = "Obtiene precios de criptomonedas en tiempo real."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "crypto",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Símbolo de la criptomoneda (ej. BTC, ETH)"},
                "currency": {"type": "string", "description": "Moneda de referencia (ej. USD, EUR)", "default": "USD"}
            },
            "required": ["symbol"]
        }
    }
}

def run(symbol: str, currency: str = "USD") -> str:
    import httpx
    try:
        # Usaremos la API de CoinGecko como ejemplo (API pública y gratuita para un uso limitado)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies={currency.lower()}"
        response = httpx.get(url, timeout=10)
        response.raise_for_status() # Lanza una excepción para códigos de estado HTTP erróneos
        data = response.json()

        if symbol.lower() in data and currency.lower() in data[symbol.lower()]:
            price = data[symbol.lower()][currency.lower()]
            return f"El precio actual de {symbol.upper()} es {price} {currency.upper()}.
            (Fuente: CoinGecko)"
        else:
            return f"No se pudo obtener el precio para {symbol.upper()} en {currency.upper()}. Verifica el símbolo."
    except httpx.RequestError as e:
        return f"Error de conexión al obtener el precio de la criptomoneda: {e}"
    except httpx.HTTPStatusError as e:
        return f"Error HTTP al obtener el precio de la criptomoneda: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"Error inesperado al obtener el precio de la criptomoneda: {e}"
