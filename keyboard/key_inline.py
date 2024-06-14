from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random


def get_keyboard_random():
    keyboard_inline_not_url1 = InlineKeyboardMarkup(row_width=1)
    random_num = InlineKeyboardButton('Случайное число', callback_data='send_random_number')
    keyboard_inline_not_url1.add(random_num)
    return keyboard_inline_not_url1


def get_keyboard_inline_ege():
    keyboard_inline_ege = InlineKeyboardMarkup(row_width=2)
    EGA_1 = InlineKeyboardButton('Решу ЕГЭ - инфа', url='https://inf-ege.sdamgia.ru/')
    EGA_2 = InlineKeyboardButton('Решу ЕГЭ - профиль', url='https://math-ege.sdamgia.ru/')
    EGA_3 = InlineKeyboardButton('Решу ЕГЭ - русский', url='https://rus-ege.sdamgia.ru/')
    keyboard_inline_ege.add(EGA_1)
    keyboard_inline_ege.add(EGA_2)
    keyboard_inline_ege.add(EGA_3)
    return keyboard_inline_ege

def get_picture_start():
    keyboard_inline_start_picture = InlineKeyboardMarkup(row_width=1)
    start_image_1 = InlineKeyboardButton('start_picture', callback_data='start_picture')
    keyboard_inline_start_picture.add(start_image_1)
    return keyboard_inline_start_picture

def get_picture_stop():
    keyboard_inline_stop_picture = InlineKeyboardMarkup(row_width=1)
    stop_image_1 = InlineKeyboardButton('stop_picture', callback_data='stop_picture')
    keyboard_inline_stop_picture.add(stop_image_1)
    return keyboard_inline_stop_picture


def get_GPT_start():
    keyboard_inline_start_GPT = InlineKeyboardMarkup(row_width=1)
    start_text_1 = InlineKeyboardButton('startGPT', callback_data= 'startGPT')
    keyboard_inline_start_GPT.add(start_text_1)
    return keyboard_inline_start_GPT

def get_GPT_stop():
    keyboard_inline_stop = InlineKeyboardMarkup(row_width=1)
    stop_text = InlineKeyboardButton('stopGPT', callback_data= 'stopGPT')
    keyboard_inline_stop.add(stop_text)
    return keyboard_inline_stop