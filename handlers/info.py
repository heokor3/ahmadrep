from aiogram import types, Dispatcher
from aiogram.utils.markdown import italic, text, bold, spoiler


# @dp.message_handler(commands=["info"])
async def info(message: types.Message):
    # await message.reply("Приветствуем тебя, пользователь")
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


# @dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

def register_info(dp: Dispatcher):
    dp.register_message_handler(info, commands=[''])