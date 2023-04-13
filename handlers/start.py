from aiogram import types


# @dp.message_handler(commands=["start", "go"])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()

    kb.add(types.InlineKeyboardButton("О нас", callback_data="about"))
    # print(dir(message.from_user))
    first_name = message.from_user.first_name
    id = message.from_user.id
    await message.answer(
        "Приветствуем тебя, пользователь {first_name}, {id}",
        reply_markup=kb
    )


async def about(cb: types.CallbackQuery):
    await cb.message.delete()
    await cb.message.answer("О нас")
