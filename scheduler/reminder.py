from aiogram import types
from config import scheduler, bot


async def start_reminder(message: types.Message):
    """
        Функция для добавления напоминалки
        """
    text = message.text[8:]
    chat_id = message.from_user.id
    scheduler.add_job(remind_handler, 'interval', seconds=5, args=(text, chat_id,))
    await message.answer(text='okay')


async def remind_handler(text, chat_id,):
    """
        функция срезает слово "Напомнить" и отправляет его
        """
    print('ok')
    await bot.send_message(
        chat_id=chat_id,
        text=text)