from aiogram import types


async def check_user_is_admin(message: types.Message):
    '''
    Функция для проверки прав админа
    '''

    admins = await message.chat.get_administrators()
    for admin in admins:
        if admin['user']['id'] == message.from_user.id:
            return True
    return False


async def yes_no(message: types.Message):
    '''
    функция которая обрабатывает ответы админов и удаляет пользователя
    '''
    if message.chat.type != 'private':
        admin_ans = await check_user_is_admin(message)
        print(admin_ans)
        if admin_ans and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id
            )