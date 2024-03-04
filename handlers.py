# -*- coding: utf-8 -*-
import datetime as dt

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from keyboards import commands_keyboard,\
    start_commands, \
    client_experience_commands,\
    client_goal_commands, client_comfort_place
from fsm import OtherStates, TryingStates

from sheets import worksheet_other, worksheet_try


router = Router()


@router.message(Command("start"))
async def hello_word(message: types.Message):
    await message.answer(f'Здравствуйте !☀\n'
                         f'Я - бот женской фитнес студии «Летай»! Меня зовут Анастасия! Чем я могу помочь?',
                         reply_markup=commands_keyboard(start_commands))


@router.message(F.text.lower() == 'другое')
async def choose_other(message: types.Message, state: FSMContext):
    await message.answer(f'Давайте сначала с Вами познакомимся!\n'
                         f'Как могу к Вам обращаться?',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(OtherStates.client_name)


@router.message(OtherStates.client_name)
async def input_clientname(message: types.Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer(f'Рада знакомству!, {message.text}✨\n'
                         f'Оставьте свой номер телефона, с Вами свяжется старший администратор!\n'
                         f'Формат: 89123456789',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(OtherStates.client_phone)


@router.message(OtherStates.client_phone)
async def input_phonenumber(message: types.Message, state: FSMContext):
    await state.update_data(client_phone=message.text)
    user_data = await state.get_data()
    to_google_sheet = list(user_data.values())
    to_google_sheet.append(f'@{message.from_user.username}')
    to_google_sheet.append(str(dt.datetime.now())[:16])
    worksheet_other.append_row(to_google_sheet)

    await message.answer(f'Ожидайте звонка!\n'
                         f'С Вами свяжется администратор в течение часа!🙌🏻\n'
                         f'Спасибо за то, что выбираете нашу студию!🌸\n',
                         reply_markup=types.ReplyKeyboardRemove())

    await state.clear()


@router.message(F.text.lower() == 'пробное занятие')
async def trying_letay(message: types.Message, state: FSMContext):
    await message.answer(f'Рада, что Вы решили посетить нашу студию ✨\n'
                         f'Задам буквально несколько вопросов, чтобы передать всю информацию администратору! '
                         f'Подскажите, как к Вам можно обращаться?',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(TryingStates.client_name)


@router.message(TryingStates.client_name)
async def choosen_clientname_for_trying(message: types.Message, state: FSMContext):
    await state.update_data(client_name=message.text)
    await message.answer(f'Супер, рада знакомству, {message.text}\n'
                         f'Теперь оставьте свой номер телефона '
                         f'Формат: 89123456789',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(TryingStates.client_phonenumber)


@router.message(TryingStates.client_phonenumber)
async def choosen_phone_for_trying(message: types.Message, state: FSMContext):
    await state.update_data(client_phone=message.text)
    await message.answer(f'Мы на верном пути. Осталось всего 3 вопроса☺\n'
                         f'Подскажите, какой у Вас опыт тренировок?🏃🏻‍♀️',
                         reply_markup=commands_keyboard(client_experience_commands))
    await state.set_state(TryingStates.client_experince)


@router.message(TryingStates.client_experince)
async def choosen_experience_for_trying(message: types.Message, state: FSMContext):
    await state.update_data(client_experience=message.text)
    await message.answer(f'Спасибо за ответ!✨\n'
                         f'Теперь давайте определимся с целью! \n'
                         f'Чего хотите добиться от тренировок в фитнес студии «Летай»?',
                         reply_markup=commands_keyboard(client_goal_commands))
    await state.set_state(TryingStates.client_goal)


@router.message(TryingStates.client_goal)
async def choosen_goal_for_trying(message: types.Message, state: FSMContext):
    await state.update_data(client_goal=message.text)

    await message.answer(f'Мы у цели!🌸\n'
                         f'По городу у нас 4 студии:\n'
                         f'🌸Заводской проезд д.1\n'
                         f'🌸Есенина 29\n'
                         f'🌸Московское шоссе 20\n'
                         f'🌸Шереметьевская 13\n'
                         f'Какую локацию Вам удобно посещать ?',
                         reply_markup=commands_keyboard(client_comfort_place))
    await state.set_state(TryingStates.comfort_place)


@router.message(TryingStates.comfort_place)
async def choosen_comfort_place(message: types.Message, state: FSMContext):

    await state.update_data(comfort_place=message.text)
    user_data = await state.get_data()
    to_google_sheet = list(user_data.values())
    to_google_sheet.append(f'@{message.from_user.username}')
    to_google_sheet.append(str(dt.datetime.now())[:16])
    worksheet_try.append_row(to_google_sheet)
    await message.answer(f'Благодарю!✨\n'
                         f'Ожидайте звонка от Администратора в течение 2х часов.\n'
                         f'Вместе Вы выберите время и дату занятия.\n'
                         f'Спасибо за то, что выбираете нашу студию! 🌸\n',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
