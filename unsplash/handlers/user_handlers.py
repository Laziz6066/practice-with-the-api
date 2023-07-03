from unsplash.config_data.config import access_key, url
import requests
from aiogram import Dispatcher, types
from unsplash.loader import bot


async def cmd_photo(message: types.Message):
    headers = {
        "Authorization": f"Client-ID {access_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_url = data["urls"]["regular"]
        await bot.send_photo(message.chat.id, photo=image_url, caption=image_url)
        print("Random Image URL:", image_url)

    else:
        await message.answer("Попробуйте заново!")


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(cmd_photo, commands=['photo'])