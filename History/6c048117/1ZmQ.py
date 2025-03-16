from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='About me')],
                                               [KeyboardButton(text='Socials'),
                                                KeyboardButton(text='Contacts')],
                                                [KeyboardButton(text='Help')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Please, select menu point..')

socials_keyboard = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Github', callback_data='github_callback')],
  [InlineKeyboardButton(text='Vk', callback_data='vk_callback')]])

contacts_keyboard = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Email', callback_data='email_callback')]])