from aiogram import types

async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("Всё"))
    kb.add(types.KeyboardButton("Книги"), types.KeyboardButton("Сувениры"))
    await message.answer(
        f"Выберите категорию ниже:",
        reply_markup=kb
    )

async def show_books(message: types.Message):
    await message.reply(
        "Вот наши книги",
        reply_markup=types.ReplyKeyboardMarkup()
    )


