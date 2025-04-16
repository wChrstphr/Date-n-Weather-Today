import pytz
from datetime import datetime

def get_brasilia_time():
    return datetime.now(pytz.timezone('America/Sao_Paulo'))

def get_season(month, day):
    if (month == 12 and day >= 21) or (month <= 2) or (month == 3 and day <= 20):
        return "Summer ☀️"
    elif (month == 3 and day >= 21) or (month <= 5) or (month == 6 and day <= 20):
        return "Autumn 🍂"
    elif (month == 6 and day >= 21) or (month <= 8) or (month == 9 and day <= 20):
        return "Winter ❄️"
    else:
        return "Spring 🌸"

def format_datetime(current_time, months_dict):
    return {
        "formatted_date": f"{months_dict[current_time.month]} {current_time.day}, {current_time.year}",
        "formatted_time": current_time.strftime("%H:%M"),
        "season": get_season(current_time.month, current_time.day)
    }
