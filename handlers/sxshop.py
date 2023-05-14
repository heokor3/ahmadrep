from aiogram import types
from db.base import get_products
from time import sleep


async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("финик"))
    await message.answer(
        f"Выберите категорию ниже:",
        reply_markup=kb
    )
async def show_finik(message: types.Message):
    for product in get_products():
        await message.reply_photo(open(product[2],'rb'), caption=f'''
    Марка - {product[0]}
    Цена - {product[1]}
    ''')
        sleep(3)
    await message.delete()
