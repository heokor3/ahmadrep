from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from db.base import insert_survey


# Finite State Machine
class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    marry = State()
    obman = State()
    devushki = State()
    lohatron = State()


async def start_survey(message: types.Message):
    await Survey.name.set()

    await message.answer("Как вас зовут?")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Survey.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Введи только цифры!")
    elif int(age) > 100 or int(age) < 10:
        await message.answer("Введи нормальный возраст")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
            print(data)

        await Survey.next()

        kb = types.ReplyKeyboardMarkup()
        kb.add("Мужской", "Женский")
        await message.answer("Ваш пол?", reply_markup=kb)


async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    await Survey.next()

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('да', callback_data='yes'),
           types.InlineKeyboardButton('нет', callback_data='nou'))
    await message.answer("состоял ли ты в отношениях?", reply_markup=kb)

#
# async def process_marry(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'yes':
#         """обработчи yes"""
#         async with state.proxy() as data:
#             data['marry'] = 'yes'
#             await callback.message.answer('лох!')
#             kb = types.InlineKeyboardMarkup(row_width=2)
#             kb.add(types.InlineKeyboardButton('images/дом1.jpg', callback_data='дом1'),
#                    types.InlineKeyboardButton(text = open('images/дом2.jpg', 'rb'), callback_data='ад')),
#             kb.add(types.InlineKeyboardButton(text = open('images/дом3.jpg', 'rb'), callback_data='дом3'),
#                    types.InlineKeyboardButton(text = open('images/дом4.jpg', 'rb'), callback_data='дом4'))
#         await Survey.next()
# async def process_marry(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'yes':
#         """обработчи yes"""
#         async with state.proxy() as data:
#             data['marry'] = 'yes'
#             await callback.message.answer('лох!')
#             kb = types.InlineKeyboardMarkup(row_width=2)
#             with open('images/дом1.jpg', 'rb') as photo:
#                 kb = types.InlineKeyboardMarkup(row_width=2)
#                 kb.add(types.InlineKeyboardButton(text='дом1', callback_data='дом1'))
#                 await callback.answer_photo(photo=photo, caption='дом1', reply_markup=kb)
#             with open('images/дом2.jpg', 'rb') as photo:
#                 kb = types.InlineKeyboardMarkup(row_width=2)
#                 kb.add(types.InlineKeyboardButton(text='дом2', callback_data='дом2'))
#                 await callback.answer_photo(photo=photo, caption='дом2', reply_markup=kb)
#             with open('images/дом3.jpg', 'rb') as photo:
#                 kb = types.InlineKeyboardMarkup(row_width=2)
#                 kb.add(types.InlineKeyboardButton(text='дом3', callback_data='дом3'))
#                 await callback.answer_photo(photo=photo, caption='дом3', reply_markup=kb)
#             with open('images/дом4.jpg', 'rb') as photo:
#                 kb = types.InlineKeyboardMarkup(row_width=2)
#                 kb.add(types.InlineKeyboardButton(text='дом4', callback_data='дом4'))
#                 await callback.answer_photo(photo=photo, caption='дом4', reply_markup=kb)


async def process_marry(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'yes':
        """Это обработчик yes"""

        async with state.proxy() as data:
            data['marry'] = 'yes'
            # await callback.message.answer('лох!')
            kb = types.InlineKeyboardMarkup(row_width=2)
            kb.add(types.InlineKeyboardButton('девушку', callback_data='female'),
                   types.InlineKeyboardButton('парня', callback_data='male')),
            await Survey.next()
            await callback.message.answer('кого ищите?', reply_markup=kb)
    elif callback.data == 'nou':
        """Это обработчик nou"""
        async with state.proxy() as data:
            data['marry'] = 'nou'
            await callback.message.answer('долго лучше не жить одному')
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton('нет', callback_data='lohaotvt'),
                   types.InlineKeyboardButton('да', callback_data='damarry')),
            await Survey.next()
            await callback.message.answer('согласен?', reply_markup=kb)

async def process_obman(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['obman'] = callback.text
        await Survey.next()

        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton('да', callback_data='loshara'),
               types.InlineKeyboardButton('нет', callback_data='urod'))
        # await callback.message.answer('у тебя 0% шансев найти пару')
        # await callback.message.answer("если закинешь деньги на этот номер, то у тебя 100% шанс найти пару")
        # await callback.message.answer('+996 770 762 716')
        await callback.message.answer("закинул?", reply_markup=kb)
# async def process_obman(callback: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         data['obman'] = callback.data
#         if callback.data == 'male' or callback.data == 'female':
#             await callback.message.answer("Базар жок!")
#         elif callback.data == 'lohaotvt' or callback.data == 'damarry':
#             await callback.message.answer('u stupid')
#         else:
#             await callback.message.answer('u stupid')
#
#     await Survey.next()
#     await callback.message.answer('Сколько вы работаете в этой сфере?')
async def process_lohatron(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'loshara':
        """обработчи loshara"""
        async with state.proxy() as data:
            data['lohatron'] = 'loshara'
            await callback.message.answer('а твои шансы явно увеличелись')

            kb = types.InlineKeyboardMarkup(row_width=3)
            kb_buttons = [
                types.InlineKeyboardButton(text='Девушка 1', callback_data='dv1'),
                types.InlineKeyboardButton(text='Девушка 2', callback_data='dv2'),
                types.InlineKeyboardButton(text='Девушка 3', callback_data='dv3'),
                types.InlineKeyboardButton(text='Девушка 4', callback_data='dv4')
            ]
            kb.add(*kb_buttons)

            with open('images/девушка1.png', 'rb') as photo:
                await callback.message.answer_photo(photo=photo, caption='Девушка 1')
            with open('images/девушка2.png', 'rb') as photo:
                await callback.message.answer_photo(photo=photo, caption='Девушка 2')
            with open('images/девушка3.png', 'rb') as photo:
                await callback.message.answer_photo(photo=photo, caption='Девушка 3')
            with open('images/девушка4.png', 'rb') as photo:
                await callback.message.answer_photo(photo=photo, caption='Девушка 4')

        await Survey.next()
        await callback.message.answer('вот одинокие люди поблизости', reply_markup=kb)

    elif callback.data == 'urod':
        """Это обработчик urod"""
        async with state.proxy() as data:
            data['lohatron'] = 'urod'
            await callback.message.answer('к сожалению поблизости нет никого кто заинтересовался тобой')
            await state.finish()


# для девушек сделаю позже
async def process_devushki(callback: types.CallbackQuery, state: FSMContext):
    '''ответы на выбор девушки'''
    async with state.proxy() as data:
        data['devushki'] = callback.data
        if callback.data == 'dv1':
            await callback.message.answer("неплохой выбор!")
        elif callback.data == 'dv2':
            await callback.message.answer('снокшебательная!')
        elif callback.data == 'dv3':
            if callback.data == 'yes':
                await callback.message.answer('твоя бывшая!')
            elif callback.data == 'nou':
                await callback.message.answer('фу ты че !')
        elif callback.data == 'dv4':
            await callback.message.answer('красивая')
        else:
            await callback.message.answer('ой дура(к)')
    await callback.message.answer('спасибо за то что прошли этот опрос?')
    await state.finish()
