from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://vk.com/id328844923')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://vk.com/kristina_logutova')
ikb.add(ib1, ib2)

async def on_startup(_):
    print('bot used')

@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello world',
                           reply_markup=ikb)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)