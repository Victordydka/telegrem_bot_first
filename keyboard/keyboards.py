from aiogram.types import ReplyKeyboardMarkup, KeyboardButton           #маркап клавиатура (кнопки около строки ввода)

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)    #для того чтобы кнопки были (маркап клавиатура)
                                                            # одноразмерные на разных девайсах
    button_1 = KeyboardButton('Отправь фото дерзко')
    button_2 = KeyboardButton('Перейти на следующую клавиатуру')
    button_3 = KeyboardButton('Отправь фото арнольда')
    button_3_1 = KeyboardButton('Расскажи анекдот')
    keyboard.add(button_1, button_2, button_3, button_3_1)
    return keyboard


def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)

    button_4 = KeyboardButton('Отправь фото природы')
    button_5 = KeyboardButton('Вернуться на первую клавиатуру')
    button_6 = KeyboardButton('Отправь фото macana')
    keyboard_2.add(button_4, button_5, button_6)
    return keyboard_2