import os
from dotenv import load_dotenv


load_dotenv('.env')
bot_token = os.getenv('TOKEN')
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
url = os.getenv("URL")

