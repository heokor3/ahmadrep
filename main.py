from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp, scheduler
from handlers.info import info, echo
from handlers.start import start,about
from handlers.sxshop import show_categories, show_finik
from handlers.survey_fsm import (
    start_survey,
    process_age,
    Survey,
    process_gender,
    process_name,
    process_marry,
    process_devushki,
    process_lohatron,
    process_obman
    )
from chatbot.ban import yes_no
from chatbot.bad_wrds import filter_messages

from aiogram.contrib.fsm_storage import memory
from scheduler.reminder import start_reminder
import logging
from db.base import (
create_table_cars,
init_db

)

from parsing.cars import get_cars
from parsing.answers_cars import show_cars


async def startup(_):
    init_db()
    create_table_cars()
    get_cars()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # обработчики
    dp.register_message_handler(start, commands=[f"start"])
    dp.register_callback_query_handler(show_categories, lambda cb: cb.data == "shop")
    dp.register_message_handler(info, commands=["info"])
    dp.register_message_handler(show_categories, commands=["shop"])
    dp.register_message_handler(show_finik, Text(equals="финики"))
    dp.register_callback_query_handler(about, lambda cb: cb.data == "about")
    dp.register_message_handler(start_survey, commands='surv')
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_gender, state=Survey.gender)
    dp.register_callback_query_handler(process_marry, state=Survey.marry)
    dp.register_message_handler(process_obman, state=Survey.obman)
    dp.register_callback_query_handler(process_devushki, state=Survey.devushki)
    dp.register_message_handler(process_lohatron, state=Survey.lohatron)
    dp.register_message_handler(start_reminder, Text(startswith='напомни'))
    dp.register_message_handler(show_cars, commands=['cars'])
    dp.register_message_handler(yes_no, commands=['забанить'], commands_prefix=['!'])
    dp.register_message_handler(filter_messages)


    dp.register_message_handler(echo)
    scheduler.start()
    executor.start_polling(dp, )