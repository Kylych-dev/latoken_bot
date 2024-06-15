from aiogram import Bot, types, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties

from datetime import datetime, timedelta

import asyncio, sys, logging, openai


from core import settings
from date_info import (
    get_current_datetime,
    next_friday,
    technologies_used
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
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)
    logging.info("Установлены пользовательские команды бота")

# _______________________________________

@dp.message(Command(commands=["technologies"]))
async def command_technologies(message: types.Message):
    tech_list = '\n'.join(technologies_used)

@dp.message(Command(commands=['chat']))
async def command_chat(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! Я готов общаться. Что хотите спросить?')


@dp.message(Command(commands=['hackathon']))
async def command_hackathon(message: types.Message):
    current_time, current_date = get_current_datetime()
    next_friday_date = next_friday()
    # days_until_next_friday = current_date - next_friday_date
    # await message.answer(f'До следущего хакатона {message.from_user.full_name}!')

    days_until_next_friday = (next_friday_date - datetime.now().date()).days
    await message.answer(
        f'Сейчас {current_time} {current_date}. До ближайшего хакатона осталось {days_until_next_friday} дней.')


@dp.message()
async def message_handler(message: types.Message):
    if message.text.startswith('/chat'):
        return
    try:
        response = openai.ChatCompletion.create(
            model='gpt-4o',
            # prompt=message.text,
            max_tokens=100,
            messages=[
                {
                    'role': 'user',
                    'content': message.text,
                    # 'role': 'system',
                    # 'content': prompt

                }
            ]
        )
        await message.answer(response.choices[0].message['content'])
    except Exception as ex:
        logging.error(f"Error processing message: {ex}")
        await message.answer("Произошла ошибка при обработке запроса. Попробуйте позже.")


async def main():
    bot = Bot(token=settings.BOT_TOKEN, debug=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # await dp.start_polling(bot, skip_updates=True)

    await set_commands(bot)  # Устанавливаем команды перед запуском бота
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

