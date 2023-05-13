from aiogram import types


# @dp.message_handler(commands=["pic"])
async def picture(message: types.Message):
    with open('images/cat.webp', 'rb') as photo:
        await message.reply_photo(
            photo,
            caption="Умный кот 😂😼"
        )


# @dp.message_handler(commands=["sticker"])
async def sticker(message: types.Message):
    await message.answer_sticker("CAACAgIAAxkBAAEIhVxkMuljwGZFnSoou7p4LED1AAHHjWgAAtguAAK1LqFLRUS7pDThxU8vBA")
    await message.answer("Sticker cat")

