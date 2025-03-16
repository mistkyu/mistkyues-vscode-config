from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='About me')],
                                               [KeyboardButton(text='Socials'),
                                                KeyboardButton(text='Contacts')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Select, what you want to know about me..)')

socials_keyboard = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Github', callback_data='github_callback')],
  [InlineKeyboardButton(text='Vk', callback_data='vk_callback')]])