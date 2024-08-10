from os import getenv

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.types import Message, BotCommand
from aiogram.utils.markdown import *
from aiogram.client.bot import *
from dotenv import load_dotenv
from .routers import *     
from .routers.clothes import clothes_router

load_dotenv()

root_router = Router()
root_router.include_router(clothes_router)


@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Вітаю у нашому боті: {hbold(message.from_user.full_name)}!")



async def main() -> None:
    TOKEN = getenv("BOT_TOKEN")
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode = ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(root_router)

    await dp.start_polling(bot)