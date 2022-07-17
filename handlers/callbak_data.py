from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import random

Price1 = 199

url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPqQrwjtboYxiYG7w5Uodqnrq6nCDhArcSus6D7nhG7kPS881bTmqTJEqUZzkuKVam54iPF49jXF2kZoZXD3nFzN7EG1BkbpUEJdPk9oYFX'


@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat_exit = types.InlineKeyboardButton(text='👈 НАЗАД', callback_data='bat_exit')

    if call.data == 'bat_1':
        price = f'&amount={Price1}'
        finish_url = url+key+price
        bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ', url = finish_url)
        markup.add(bat_pay)
        markup.add(bat_exit)
        await call.message.answer(text =  """<b>Тариф:</b> ВПИСКИ И СЛИВЫ (102 гб, без цезуры)
<b>Цена:</b> 199.00 RUB
<b>Срок:</b> Бессрочный
<b>Способ оплаты:</b> Карта / Qiwi
""",reply_markup=markup)


    if call.data == 'bat_exit':
        await bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)


    await bot.answer_callback_query(callback_query_id=call.id)