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
    stpdqstn = State()
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


async def process_marry(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'yes':
        """обработчи yes"""
        async with state.proxy() as data:
            data['marry'] = 'yes'
            await callback.message.answer('лох!')
            kb = types.InlineKeyboardMarkup(row_width=2)
            kb.add(types.InlineKeyboardButton(photo = open('media/дом1.jpg', 'rb'), callback_data='дом1'),
                   types.InlineKeyboardButton(photo = open('media/дом2.jpg', 'rb'), callback_data='ад')),
            kb.add(types.InlineKeyboardButton(photo = open('media/дом3.jpg', 'rb'), callback_data='дом3'),
                   types.InlineKeyboardButton(photo = open('media/дом4.jpg', 'rb'), callback_data='дом4'))
        await Survey.next()
        await callback.message.answer('какой дом выберешь?', reply_markup=kb)
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


async def process_stpdqstn(callback: types.CallbackQuery, state: FSMContext):
    '''процесс отвечает за ответы на ответы'''
    async with state.proxy() as data:
        data['stpdqstn'] = callback.data
        if callback.data == 'дом1':
            await callback.message.answer("ха бомж тебе еще копить и копить!")
        elif callback.data == 'ад':
            await callback.message.answer('ха бомж тебе еще копить и копить!')
        elif callback.data == 'дом3':
            await callback.message.answer('ха бомж тебе еще копить и копить!')
        elif callback.data == 'дом4':
            await callback.message.answer('очень уйютный домик,тем более по корману')
        elif callback.data == 'damarry':
            await callback.message.answer('а вот и молодец')
        elif callback.data == 'lohaotvt':
            await callback.message.answer('а вот и да!')
            await state.finish()
        else:
            await callback.message.answer('ой дура(к)')

    await Survey.next()
    await callback.message.answer('у тебя 0% шансев найти пару')
    await callback.message.answer("если закинешь деньги на этот номер, то у тебя 100% шанс найти пару")
    await callback.message.answer('+996 770 762 716')
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('да', callback_data='loshara'),
           types.InlineKeyboardButton('нет', callback_data='urod'))
    await callback.message.answer("закинул?", reply_markup=kb)

async def process_lohatron(callback: types.CallbackQuery, state: FSMContext):
    '''тут тот же подход что и вв мерри'''
    if callback.data == 'loshara':
        """обработчи loshara"""
        async with state.proxy() as data:
            data['lohatron'] = 'loshara'
            await callback.message.answer('а твои шансы явно увеличелись')

            kb = types.InlineKeyboardMarkup(row_width=3)
            kb.add(types.InlineKeyboardButton(photo = open('media/девушка1.png', 'rb'), callback_data='dv1'),
                   types.InlineKeyboardButton(photo = open('media/девушка2.png', 'rb'), callback_data='dv2')),
            kb.add(types.InlineKeyboardButton(photo = open('media/девушка3.png', 'rb'), callback_data='urdv3'),
                   types.InlineKeyboardButton(photo = open('media/девушка4.png', 'rb'), callback_data='dv4'))
        await Survey.next()
        await callback.message.answer('вот одинокие люди поблизости', reply_markup=kb)
    elif callback.data == 'urod':
        """Это обработчик urod"""
        async with state.proxy() as data:
            data['lohatron'] = 'urod'
            await callback.message.answer('к сожалению поблизости нет никого кто заинтересовался тобой')
            await state.finish()

async def process_devushki(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['devushki'] = callback.data
        if callback.data == 'dv1':
            await callback.message.answer("неплохой выбор!")
        elif callback.data == 'dv2':
            await callback.message.answer('снокшебательная!')
        elif callback.data == 'urdv3':
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
