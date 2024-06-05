from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

#инлайн клавиатура (кнопки по сообщениями от бота) с url

    #арнольд
def get_keyboard_inline_1():
    keyboard_1_inline = InlineKeyboardMarkup(row_width=1)     #задаём кол-во кнопок в строке
    but_inline_1 = InlineKeyboardButton('Википедия', url='https://ru.wikipedia.org/wiki/%D0%A8%D0%B2%D0%B0%D1%80%D1%86%D0%B5%D0%BD%D0%B5%D0%B3%D0%B3%D0%B5%D1%80,_%D0%90%D1%80%D0%BD%D0%BE%D0%BB%D1%8C%D0%B4')
    but_inline_2 = InlineKeyboardButton('Фильм - Терминатор', url='https://www.kinopoisk.ru/film/507/')
    keyboard_1_inline.add(but_inline_1, but_inline_2)
    return keyboard_1_inline


    #дерзко
def get_keyboard_inline_2():
    keyboard_2_inline = InlineKeyboardMarkup(row_width=1)
    but_inline_3 = InlineKeyboardButton('Не отдам - Дерзко', url='https://www.youtube.com/watch?v=1hW6JLqkYzk')
    keyboard_2_inline.add(but_inline_3)
    return keyboard_2_inline


    #macan
def get_keyboard_inline_3():
    keyboard_3_inline = InlineKeyboardMarkup(row_width=2)
    but_inline_4 = InlineKeyboardButton('Википедия', url='https://ru.wikipedia.org/wiki/Macan')
    but_inline_5 = InlineKeyboardButton('Трек - Брат', url='https://www.youtube.com/watch?v=O20mHKAogs8')
    but_inline_6 = InlineKeyboardButton('Трек - solo2', url='https://www.youtube.com/watch?v=braiYbiM6oU')
    but_inline_7 = InlineKeyboardButton('Трек - пьяный округ', url='https://www.youtube.com/watch?v=40lGUYTR8qQ')
    but_inline_8 = InlineKeyboardButton('Трек - За всех', url='https://www.youtube.com/watch?v=q2s2KyqwoHs')
    keyboard_3_inline.add(but_inline_8, but_inline_5, but_inline_6, but_inline_7, but_inline_4)
    return keyboard_3_inline


#инлайн клавиатура (кнопки по сообщениями от бота) без url кроме решу егэ

def get_keyboard_inline_not_url1():
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

