

import requests
import time

def analyze_eth_market(api_key, api_secret):
    url = "https://api.mexc.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data = response.json()

    eth_data = next((item for item in data if item["symbol"] == "ETHUSDT"), None)
    if not eth_data:
        return {"status": "error", "message": "ETH data not found."}

    price = float(eth_data["lastPrice"])
    change_percent = float(eth_data["priceChangePercent"])

    # Lógica Sniper + Guardian simplificada
    if change_percent > 2:
        signal = "🟢 Señal: COMPRÁ CALL para ETH (exp. 3 días). Momentum positivo fuerte."
    elif change_percent < -2:
        signal = "🔴 Señal: COMPRÁ PUT para ETH (exp. 3 días). Caída detectada."
    else:
        signal = "🟡 No hay señal clara ahora. Esperando mejor entrada."

    return {
        "status": "ok",
        "price": price,
        "change": change_percent,
        "signal": signal,
        "timestamp": int(time.time())
    }