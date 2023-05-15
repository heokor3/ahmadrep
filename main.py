from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp, scheduler
from handlers.images import picture,sticker
from handlers.info import info, echo
from handlers.start import start,about
from handlers.sxshop import show_categories, show_finik
from handlers.survey_fsm import (
    start_survey,
    age,
    Survey,
    gender,
    name,
    inter,
    cancel,
    photo,
    submit
    )
from chatbot.ban import yes_no
from chatbot.bad_wrds import filter_messages

from aiogram.contrib.fsm_storage import memory
from scheduler.reminder import start_reminder
import logging
from db.base import (
init_db
)

from parsing.parser import get_news



async def startup(_):
    init_db()
    get_news()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # обработчики
    dp.register_message_handler(start, commands=[f"start"])
    dp.register_callback_query_handler(show_categories, lambda cb: cb.data == "shop")
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_finik, Text(equals="финик"))
    dp.register_callback_query_handler(about, lambda cb: cb.data == "about")
    dp.register_message_handler(cancel,Text(equals='cancel', ignore_case=True) , state='*')
    dp.register_message_handler(start_survey, commands=['surv'])
    dp.register_message_handler(name, state=Survey.name)
    dp.register_message_handler(age, state=Survey.age)
    dp.register_message_handler(gender, state=Survey.gender)
    dp.register_message_handler(inter, state=Survey.interested)
    dp.register_message_handler(photo, state=Survey.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=Survey.submit)
    dp.register_message_handler(start_reminder, Text(startswith='напомни'))
    dp.register_message_handler(get_news, commands=['news'])
    dp.register_message_handler(yes_no, commands=['забанить'], commands_prefix=['!'])
    dp.register_message_handler(filter_messages)


    dp.register_message_handler(echo)
    scheduler.start()
    executor.start_polling(dp, )