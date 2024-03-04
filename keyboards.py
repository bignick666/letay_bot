from aiogram import types


start_commands = ['Пробное занятие', 'Другое']
# approve_commands = ['Да', 'Нет']
client_experience_commands = ['Нет опыта', '1-12 месяцев', 'Более 12 месяцев']
client_goal_commands = ['Похудеть', 'Подтянуть тело', 'Расслабиться', 'Здоровую спину']
client_comfort_place = ['Заводской', 'Московский', 'Есенина', 'Шереметьевская']


def commands_keyboard(commands):
    kb = [types.KeyboardButton(text=item) for item in commands]
    return types.ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)
