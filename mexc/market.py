


import requests
import time

MEXC_BASE_URL = "https://api.mexc.com"

def get_eth_price():
    try:
        response = requests.get(f"{MEXC_BASE_URL}/api/v3/ticker/price?symbol=ETHUSDT")
        response.raise_for_status()
        price = float(response.json()["price"])
        return price
    except Exception as e:
        from logs.logger import log_error
        log_error(f"Error al obtener precio ETH: {str(e)}")
        return None

def get_price_change(symbol="ETHUSDT", interval="1h"):
    try:
        endpoint = f"/api/v3/klines"
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": 2
        }
        response = requests.get(f"{MEXC_BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        data = response.json()
        if len(data) < 2:
            return 0.0
        open_price = float(data[-2][1])
        close_price = float(data[-1][4])
        change = ((close_price - open_price) / open_price) * 100
        return round(change, 2)
    except Exception as e:
        from logs.logger import log_error
        log_error(f"Error al calcular cambio de precio: {str(e)}")
        return 0.0