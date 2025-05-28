import requests
import datetime

# Configuración Telegram
TELEGRAM_TOKEN = "7816703837:AAGBFm5rTW4H9n-VJ6rbSi3t2-WebsWc_Xo"
CHAT_ID = "7613460488"

def send_signal(message, prefix="📡 Señal AI"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"{prefix} – {timestamp}\n\n{message}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"[Messenger Error] {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    send_signal("🔥 Oportunidad detectada: comprá CALL para el 5/30, strike $65.5.\nAcción sugerida: ENTRAR AHORA.")
