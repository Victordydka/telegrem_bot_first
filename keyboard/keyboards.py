from aiogram.types import ReplyKeyboardMarkup, KeyboardButton           #маркап клавиатура (кнопки около строки ввода)

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)    #для того чтобы кнопки были (маркап клавиатура) одноразмерные на разных девайсах
    button_1 = KeyboardButton('Сгенерировать ответ на вопрос')
    button_2 = KeyboardButton('Сгенерировать картинку')
    button_3 = KeyboardButton('Рандомайзер чисел')
    keyboard.add(button_1, button_2, button_3)
    return keyboard
