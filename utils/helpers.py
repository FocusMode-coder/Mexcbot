


import datetime
import pytz

def get_current_time_formatted(timezone='America/Los_Angeles'):
    """Returns the current time in the given timezone as a formatted string."""
    tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

def format_signal_message(token, action, strike, expiry, confidence, price=None):
    """
    Creates a well-formatted message for a trading signal.
    """
    msg = f"📡 Señal detectada:\n"
    msg += f"🪙 Activo: {token}\n"
    msg += f"📈 Acción: {action}\n"
    msg += f"🎯 Strike: {strike}\n"
    msg += f"📅 Expira: {expiry}\n"
    msg += f"💡 Confianza: {confidence}%\n"
    if price:
        msg += f"💰 Precio actual: ${price}\n"
    msg += f"⏰ {get_current_time_formatted()}"
    return msg