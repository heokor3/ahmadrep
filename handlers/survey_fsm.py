from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    interested = State()
    photo = State()
    submit = State()
    cancel = State()


cancel_but = types.KeyboardButton('cancel')
kb_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_but)


async def start_survey(message: types.Message):
    await Survey.name.set()
    await message.answer('Как вас зовут?', reply_markup=kb_cancel)


async def name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Survey.next()
    await message.answer('Сколько вам лет?')


kb_gen = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    types.KeyboardButton('мужлан'),
    types.KeyboardButton('посудомойка'),
    types.KeyboardButton('не знаю')).add(  # что бы никого не ущимлять
    cancel_but)


async def age(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if 100 > int(message.text) > 10:
            async with state.proxy() as data:
                data['age'] = message.text
            await Survey.next()
            await message.answer('какого вы пола?', reply_markup=kb_gen)
        else:
            await message.answer('Вводи нормальный возраст', reply_markup=kb_cancel)
    else:
        await message.answer('Вводите толко числа', reply_markup=kb_cancel)


kb_int = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    types.KeyboardButton('мужчина'),
    types.KeyboardButton('женщина'),
    types.KeyboardButton('без разницы')).add(cancel_but)


async def gender(message: types.Message, state: FSMContext):
    if message.text in ['мужлан', 'посудомойка', 'не знаю']:
        async with state.proxy() as data:
            data['gender'] = message.text
        await message.answer('кто тебя интересует🤭',  # заигрываем
                             reply_markup=kb_int)
        await Survey.next()
    else:
        await message.answer('Балбес, выбирай из того что есть', reply_markup=kb_gen)


async def inter(message: types.Message, state: FSMContext):
    if message.text in ['мужчина', 'женщина', 'без разницы']:
        async with state.proxy() as data:
            data['interested'] = message.text
            await message.answer('Скинь фотку ; )', reply_markup=kb_cancel)
            await Survey.next()
    else:
        await message.answer('Выибрай из списка дуралей',
                             reply_markup=kb_int)


kb_submit = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                      one_time_keyboard=True).add(
    types.KeyboardButton('да'),
    types.KeyboardButton('нет'))


async def photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Survey.next()
    await message.answer_photo(photo=data['photo'], caption=
    f"{data['name']}\n"
    f"{data['age']} лет\n"
    f"{data['gender']}\n"
    f"интересуется в {data['interested']}\n")
    await message.answer('все правильно?', reply_markup=kb_submit)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await message.answer('круто')
        await state.finish()
    elif message.text.lower() == 'нет':
        await message.answer('ну и пошел ты')
        await state.finish()
    else:
        await message.answer('выбирай из списка ишак полосатый', reply_markup=kb_submit)


async def cancel(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is not None:
        await state.finish()
        await message.answer('ну и пошел ты')

# dp.register_message_handler(cancel,Text(equals='cancel', ignore_case=True) , state='*')
# dp.register_message_handler(start_survey, commands=['surv'])
# dp.register_message_handler(name, state=Survey.name)
# dp.register_message_handler(age, state=Survey.age)
# dp.register_message_handler(gender, state=Survey.gender)
# dp.register_message_handler(inter, state=Survey.interested)
# dp.register_message_handler(photo, state=Survey.photo, content_types=['photo'])
# dp.register_message_handler(submit, state=Survey.submit)
