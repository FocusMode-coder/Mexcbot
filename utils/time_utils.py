


from datetime import datetime, timedelta

def get_current_time(format_24h=True):
    now = datetime.now()
    return now.strftime("%H:%M:%S") if format_24h else now.strftime("%I:%M:%S %p")

def is_market_open():
    now = datetime.utcnow() - timedelta(hours=4)  # Convert UTC to ET
    if now.weekday() >= 5:  # Saturday or Sunday
        return False
    open_time = now.replace(hour=9, minute=30, second=0, microsecond=0)
    close_time = now.replace(hour=16, minute=0, second=0, microsecond=0)
    return open_time <= now <= close_time

def get_market_time_left():
    now = datetime.utcnow() - timedelta(hours=4)  # Convert UTC to ET
    close_time = now.replace(hour=16, minute=0, second=0, microsecond=0)
    if now > close_time:
        return "Market closed"
    delta = close_time - now
    return str(delta).split('.')[0]  # Return HH:MM:SS