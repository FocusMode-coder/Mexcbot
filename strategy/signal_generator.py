


import requests

def fetch_market_data(symbol="TQQQ_USDT"):
    url = f"https://api.mexc.com/api/v3/depth?symbol={symbol}&limit=50"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"[ERROR] Failed to fetch market data: {e}")
        return None

def analyze_order_book(data, threshold_ratio=1.5):
    if not data or "bids" not in data or "asks" not in data:
        return None

    total_bids = sum(float(bid[1]) for bid in data["bids"])
    total_asks = sum(float(ask[1]) for ask in data["asks"])

    if total_bids > total_asks * threshold_ratio:
        return "BUY"
    elif total_asks > total_bids * threshold_ratio:
        return "SELL"
    else:
        return "HOLD"

def generate_signal():
    market_data = fetch_market_data()
    signal = analyze_order_book(market_data)
    print(f"[SIGNAL] Current Signal: {signal}")
    return signal