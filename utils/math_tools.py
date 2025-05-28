

def calculate_percentage_change(current_price, previous_price):
    if previous_price == 0:
        return 0
    return ((current_price - previous_price) / previous_price) * 100

def round_to_decimals(value, decimals=2):
    return round(value, decimals)