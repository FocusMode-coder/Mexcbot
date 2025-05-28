import requests
import datetime

def analyze_market(ticker="ETHUSDT"):
    """
    Lógica Sniper + Guardian:
    Genera una señal de compra CALL o PUT basada en el movimiento reciente del precio.
    Devuelve una señal realista para operar en Robinhood.
    """
    try:
        url = f"https://api.mexc.com/api/v3/klines?symbol={ticker}&interval=1m&limit=5"
        response = requests.get(url)
        data = response.json()

        closes = [float(candle[4]) for candle in data]
        last_price = closes[-1]
        avg_price = sum(closes[:-1]) / len(closes[:-1])
        change = (last_price - avg_price) / avg_price * 100

        if change > 0.25:
            return {
                "type": "CALL",
                "strike": round(last_price * 1.01, 2),
                "expiry": "3 days from now",
                "confidence": f"{round(change, 2)}% de impulso positivo",
                "reason": "Impulso alcista detectado. Suba rápida en minutos recientes."
            }
        elif change < -0.25:
            return {
                "type": "PUT",
                "strike": round(last_price * 0.99, 2),
                "expiry": "3 days from now",
                "confidence": f"{round(change, 2)}% de caída rápida",
                "reason": "Retroceso abrupto. Posible corrección en curso."
            }
        else:
            return {
                "type": "HOLD",
                "reason": "Mercado lateral. Esperar confirmación de movimiento."
            }

    except Exception as e:
        return {
            "type": "ERROR",
            "message": str(e)
        }
