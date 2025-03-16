from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
  await message.answer('Hi!', reply_markup=kb.reply_keyboard) 
  await message.answer('Please, select menu point..')

@router.message(Command('help'))
async def cmd_help(message:Message):
  await message.answer('You write help command!')
  
@router.message(Command('menu'))
async def cmd_menu(message:Message):
  await message.answer('Please, select menu point..', reply_markup=kb.reply_keyboard)
  
@router.message(F.text == 'About me')
async def func_catalog_keyboard(message:Message):
  await message.answer('Please, select catalog point..', reply_markup=kb.catalog_keyboard)
  
@router.callback_query(F.data == 'github_callback')
async def func_wb_catalog(callback:CallbackQuery):
  await callback.answer('')
  await callback.message.answer('This is link to my Github: https://github.com/mistkyu')
  
@router.callback_query(F.data == 'vk_callback')
async def func_ozon_catalog(callback:CallbackQuery):
  await callback.answer('')
  await callback.message.answer('This is link to my Vk: https://vk.com/mistkyu')