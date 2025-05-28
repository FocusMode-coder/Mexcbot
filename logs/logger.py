import time
import os
from datetime import datetime

LOG_PATH = "logs/signals.log"

def log_signal(data: dict):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        timestamp = datetime.fromtimestamp(data.get("timestamp", time.time())).strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] {data.get('signal')} | Precio: ${data.get('price')} | Cambio: {data.get('change')}%\n"
        f.write(message)

def log_error(message: str):
    os.makedirs("logs", exist_ok=True)
    with open("logs/errors.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ERROR: {message}\n")