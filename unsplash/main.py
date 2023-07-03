from aiogram.utils import executor
from loader import dp
from handlers import start, user_handlers


async def on_startup(_):
    print('Бот вышел в онлайн')


start.register_handler_start(dp)
user_handlers.register_handler_start(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)