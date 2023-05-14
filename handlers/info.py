from aiogram import types, Dispatcher
from aiogram.utils.markdown import italic, text, bold, spoiler

async def info(message: types.Message):
    firstname = message.from_user.first_name
    await message.reply(
        text(
            "Приветствуем тебя",
            italic("пользователь"),
            bold(firstname),
            spoiler("я знаю о тебе все!")
        ),
        parse_mode="MarkdownV2"
    )
async def echo(message: types.Message):
    await message.answer(message.text)

def register_info(dp: Dispatcher):
    dp.register_message_handler(info, commands=[''])