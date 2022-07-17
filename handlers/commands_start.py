from aiogram import types
from misc import dp,bot
from .sqlit import reg_user
import asyncio

ids_user = []
markup = types.InlineKeyboardMarkup()

bat_1 = types.InlineKeyboardButton(text='БЕЗ ЦЕНЗУРЫ 18+ | 199.00 RUB', callback_data='bat_1')

markup.add(bat_1)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(id = message.chat.id)
    await message.answer(text="""<b>💙💦ВПИСКИ И СЛИВЫ БЕЗ ЦЕНЗУРЫ💦💙

▪️Автоматический бот🤖✅ 

▪️Анонимная покупка🤫✅

▪️Моментальный доступ😋✅</b>""",reply_markup=markup)