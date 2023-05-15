from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from db.base import insert_product, get_products

# функция отвечает за фото,цену,название,
async def get_product_cards():
    products = get_products()
    cards = []
    for product in products:
        name, price, image = product[1], product[2], product[3]
        # инлайнкнопка отвечающая за название и цену продукта
        button = InlineKeyboardButton(f"{name} ({price} руб)", callback_data=f"buy_{product[0]}")
        # инлайн кнопка отвечающая за кнопку и фото финика
        markup = InlineKeyboardMarkup()
        markup.add(button)
        cards.append({"photo": image, "caption": name, "reply_markup": markup})
    return cards


async def start(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Купить финики", callback_data="buy"))
    await message.answer("Добро пожаловать в магазин фиников!", reply_markup=markup)


async def show_products(message: types.Message):
    cards = await get_product_cards()
    for card in cards:
        # фото товара с подписью и инлайнкнопкой
        await message.answer_photo(card["photo"], caption=card["caption"], reply_markup=card["reply_markup"])


async def buy_callback_handler(query: CallbackQuery):
    await show_products(query.message)
    await query.answer()

async def buy_product_callback_handler(query: CallbackQuery):
    product_id = int(query.data.split("_")[1])
    # получение информации о продукте из бд
    products = get_products()
    product = None
    for p in products:
        if p[0] == product_id:
            product = p
            break
    if product is None:
        await query.message.answer("Произошла ошибка при попытке найти продукт.")
        return
    # отправка информации о продукте пользователю
    caption = f"ты выбрал продукт: {product[1]}\nЦена: {product[2]} сом"
    photo = product[3]
    await query.message.answer_photo(photo, caption=caption)