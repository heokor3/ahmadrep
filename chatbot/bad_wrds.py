from aiogram import types


async def filter_messages(message: types.Message):
    badwrds = ['скатина','сволочь','тварь','урод','картошка','лох','дибил']
    if message.chat.type != 'private':
        for i in badwrds:
            if i in message.text.lower().replace(' ', ''):
                await message.reply(text=f'Пользователь {message.from_user.first_name} отправил '
                                         f'запрещённое слово\n'
                                         f'Админы удалять {message.from_user.first_name}: забанить?')
                break