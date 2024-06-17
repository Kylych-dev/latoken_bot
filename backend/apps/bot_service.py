from aiogram import Bot, types, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties

from datetime import datetime, timedelta

import asyncio, sys, logging, openai


from core import settings
from utils import (
    get_current_datetime,
    next_friday,
    technologies_used,
    # scrap_website
)


# _______________________________________
# Openapi
import openai
openai.api_key = settings.OPENAI_TOKEN

# _______________________________________
dp = Dispatcher()


# _______________________________________
# Commands
commands = [
    types.BotCommand(command="/start", description="Начать взаимодействие с ботом"),
    types.BotCommand(command="/hackathon", description="Узнать сколько осталось до ближайшего хакатона"),
    types.BotCommand(command="/chat", description="Начать чат с ботом"),
    types.BotCommand(command="/technologies", description='стек который я использовал')
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)
    logging.info("Установлены пользовательские команды бота")

# _______________________________________


@dp.message(Command(commands=["technologies"]))
async def command_technologies(message: types.Message):
    tech_list = '\n'.join(technologies_used)
    print('hello im technologies')
    await message.answer(f'В проекте использованы следующие технологии:\n\n{tech_list}')


@dp.message(Command(commands=['chat']))
async def command_chat(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! Я готов общаться. Что хотите спросить?')


@dp.message(Command(commands=['hackathon']))
async def command_hackathon(message: types.Message):
    current_time, current_date = get_current_datetime()
    next_friday_date = next_friday()


    days_until_next_friday = (next_friday_date - datetime.now().date()).days
    await message.answer(
        f'Сейчас {current_time} {current_date}. До ближайшего хакатона осталось {days_until_next_friday} дней.')


@dp.message()
async def message_handler(message: types.Message):
    user_txt = message.text
    if (user_txt.startswith('/start') or
            user_txt.startswith('/hackathon') or
            user_txt.startswith('/chat') or
            user_txt.startswith('/technologies')
    ):
        return

    if 'единорогов' in user_txt.lower():
        await message.answer('hello how are you')
        return

    try:
        response = openai.ChatCompletion.create(
            model='gpt-4o',
            max_tokens=100,
            messages=[
                {
                    'role': 'user',
                    'content': message.text,

                }
            ]
        )
        await message.answer(response.choices[0].message['content'])
    except Exception as ex:
        logging.error(f"Error processing message: {ex}")
        await message.answer(
            "Произошла ошибка при обработке запроса. Попробуйте позже."
        )


async def main():
    bot = Bot(token=settings.BOT_TOKEN, debug=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # await dp.start_polling(bot, skip_updates=True)

    await set_commands(bot)  # Устанавливаем команды перед запуском бота
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

