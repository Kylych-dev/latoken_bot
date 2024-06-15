from datetime import datetime, timedelta


def next_friday():
    today = datetime.now()
    days_until_friday = (4 - today.weekday()) % 7   #кол дней до пт (0 - пятница, 4 - понедельник, ...)
    if days_until_friday == 0:
        days_until_friday =7
    next_friday = today + timedelta(days=days_until_friday)

    return next_friday.date()


def get_current_datetime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    return current_time, current_date


# technologies.py

technologies_used = [
    "Python",
    "aiogram",
    "OpenAI",
    "datetime",
    "logging",
    "asyncio",
    "Telegram API",
    "etc."
]
