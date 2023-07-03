from aiogram import Dispatcher, types


async def cmd_start(message: types.Message):
    await message.answer("Этот бот отправляет случайную фотографию нажмите /photo чтобы попробовать.")


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
