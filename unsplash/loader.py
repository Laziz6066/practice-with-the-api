from aiogram.dispatcher import Dispatcher
from config_data import config
from aiogram import Bot


bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)
