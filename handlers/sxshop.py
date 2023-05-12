from aiogram import types
from db.base import get_products
from time import sleep



async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("Часы"))
    await message.answer(
        f"Выберите категорию ниже:",
        reply_markup=kb
    )


async def show_suveniry(message: types.Message):
    i = 0
    for i in range(len(get_products())):
        product = get_products()[i]

        await message.answer_photo(open(product[3],'rb'), caption=f'''
    Марка - {product[1]} 
    Цена - {product[2]}
    ''')
        sleep(3)
    await message.delete()