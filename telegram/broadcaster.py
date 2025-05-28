

import telebot
import os

# Cargar token y chat_id desde variables de entorno o .env
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Faltan TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en el entorno.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_signal_message(text):
    """
    Envía un mensaje personalizado al chat de Telegram.
    """
    try:
        formatted_message = f"🧠 Luciano AI:\n\n{text}"
        bot.send_message(TELEGRAM_CHAT_ID, formatted_message)
        print(f"[OK] Mensaje enviado: {formatted_message}")
    except Exception as e:
        print(f"[ERROR] No se pudo enviar el mensaje a Telegram: {e}")