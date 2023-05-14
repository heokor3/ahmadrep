
from aiogram import types


# @dp.message_handler(commands=["start", "go"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("О нас", callback_data="about"),
        types.InlineKeyboardButton("Наш сайт", url="https://google.com")
    )
    await message.answer('наш адрес: Соликамская 13', reply_markup=kb)
    # print(dir(message.from_user))
    first_name = message.from_user.first_name
    id = message.from_user.id
    await message.answer(
        f"Приветствуем тебя, пользователь {first_name}, {id}",
        reply_markup=kb
    )


async def about(cb: types.CallbackQuery):
    # await cb.message.delete()
    print(cb.data)
    await cb.answer("Исчезащее сообщение")
    await cb.message.answer("О нас")