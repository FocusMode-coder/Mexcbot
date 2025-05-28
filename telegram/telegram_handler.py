

import telebot
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_telegram_signal(signal: str, price: float, recommendation: str):
    message = f"""
    🚨 Señal detectada: {signal.upper()}
    📈 Precio ETHUSDT: ${price:.2f}
    💡 Recomendación: {recommendation}

    🧠 LucianoAI Modo Dios
    """
    bot.send_message(TELEGRAM_CHAT_ID, message.strip())