from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import os
load_dotenv()
BOT_TOKEN = '6244264554:AAEhGtoAClfYP464Fd96NwXDQpDKRqf4t_E'
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
