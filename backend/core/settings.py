# settings.py
from decouple import config
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file


# Telegram bot token
BOT_TOKEN = config('BOT_TOKEN')
OPENAI_TOKEN = config('GPT_TOKEN')