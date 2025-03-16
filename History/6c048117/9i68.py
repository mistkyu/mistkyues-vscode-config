from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

reply_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Catalog')],
                                               [KeyboardButton(text='Contacts'),
                                                KeyboardButton(text='About Us')]],
                                     resize_keyboard = True,
                                     input_field_placeholder = 'Select menu point..')

catalog_keyboard = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Wildberries', callback_data='wildberries_callback')],
  [InlineKeyboardButton(text='Ozon', callback_data='ozon_callback')]])