from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Register(StatesGroup):
  name = State()
  age = State()
  phone_number = State()

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
  
@router.message(F.text == 'Catalog')
async def func_catalog_keyboard(message:Message):
  await message.answer('Please, select catalog point..', reply_markup=kb.catalog_keyboard)
  
@router.callback_query(F.data == 'wildberries_callback')
async def func_wb_catalog(callback:CallbackQuery):
  await callback.answer('')
  await callback.message.answer('You select wildberries category')
  
@router.callback_query(F.data == 'ozon_callback')
async def func_ozon_catalog(callback:CallbackQuery):
  await callback.answer('')
  await callback.message.answer('You select ozon category')
  
@router.message(Command('register'))
async def register(message:Message, state:FSMContext):
  await state.setstate(Register.name)
  await message.answer('Input your name')