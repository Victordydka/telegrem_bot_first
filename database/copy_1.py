"""
aiogram - ассинхронная библиотека использует ассинх. ф-ции (async)
Bot - обращение к боту с помощью библиотки
Dispatcher - свод правил, что бот работает по всем правилам
types - типы данных от телеграмма
executor - нужен чтобы бот беспрерывно работал
ReplyKeyboardMarkup, KeyboardButton - маркап клавиатура
InlineKeyboardButton, InlineKeyboardMarkup - инлайн клавиатура
random - нужен для генерации рандомных чисел
"""
import random
from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1
from keyboard.key_inline import get_keyboard_inline_ege, get_keyboard_random, get_GPT_start, get_GPT_stop, get_picture_start, get_picture_stop
from database.data_base import initialize_db, add_user, get_user
from neironka.picture_bot import generate_image
from neironka.yandex_gpt_bot import generate_text


bot = Bot(token=TELEGRAM_TOKEN)     #токен бота=нашему токену
dp = Dispatcher(bot)  #означает что бот будет соответствовать всем правилам

initialize_db()     #запустили базу данных

#как человек нажал команду старт, то мы создаем переменную user
#и с помощью get_user будем заносить нашу информацию из from_user.id
@dp.message_handler(commands='start')           #обращениие к телеге
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я твой бот, который сгенерирует картинки, ответит на любые задающие вопросы,'
                             'напишет реферат или сгенерирует рандомное число, при надобности перекинет на нужный предмет для подготовки к ЕГЭ.   '
                             'Скорее попробуй меня;)', reply_markup=get_keyboard_1())


    else:
        await message.answer('Привет, я твой бот, который сгенерирует картинки, ответит на любые задающие вопросы,'
                             'напишет реферат или сгенерирует рандомное число, при надобности перекинет на нужный предмет для подготовки к ЕГЭ.   '
                             'Скорее попробуй меня;)', reply_markup=get_keyboard_1())


#команда егэ
@dp.message_handler(commands='ege')
async def ege(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://kabinet-lichnyj.ru/wp-content/uploads/2021/05/1-58.jpg', caption='Я помогу тебе с ЕГЭ', reply_markup=get_keyboard_inline_ege())


#Рандомайзер чисел от 1 до 100
@dp.message_handler(lambda message: message.text == 'Рандомайзер чисел')
async def random_number(message: types.Message):
    await message.answer('Генерация рандомных чисел от 1 до 100', reply_markup=get_keyboard_random())

@dp.callback_query_handler(lambda c: c.data == 'send_random_number')    #lambda - функция сравнения
async def send_random_number(callback_query: types.CallbackQuery):
    send_random_num = random.randint(1, 100)
    await callback_query.message.answer(f'Ваше случайное число: {send_random_num}')


#кастомное меню (со всеми командами)
async def set_comands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для запуска бота'),
        types.BotCommand(command='/ege', description='Ссылки на решу егэ')
    ]
    await bot.set_my_commands(commands)

# Генерация картинок с помощью yandex gpt
picture_generation_state = False
@dp.message_handler(lambda message: message.text == 'Сгенерировать картинку')
async def button_3_click(message: types.Message):
    await message.answer('Нажми на СТАРТ и напиши что тебе нужно сгенерировать', reply_markup= get_picture_start())

@dp.callback_query_handler(lambda callback_data: callback_data.data == 'start_picture')
async def start_picture(callback_query: types.CallbackQuery):
    global picture_generation_state
    if not picture_generation_state:
        picture_generation_state = True
        await callback_query.message.answer('Генерация картинок работает, напиши мне задачу')
    else:
        picture_generation_state = True
        await callback_query.message.answer('Я зарабтал')

@dp.callback_query_handler(lambda callback_data: callback_data.data == 'stop_picture')
async def stop_picture(callback_query: types.CallbackQuery):
    global picture_generation_state
    if picture_generation_state:
        picture_generation_state = False
        await callback_query.message.answer('Генерация картинок приостановила работу')
    else:
        picture_generation_state = False
        await callback_query.message.answer('Приостановил работу')

#Генерация текста с помощью yandex gpt
gpt_generation_state = False
@dp.message_handler(lambda message: message.text == 'Сгенерировать ответ на вопрос')
async def button_1_click(message: types.Message):
    await message.answer('Нажми на СТАРТ и задай свой вопрос', reply_markup=get_GPT_start())

@dp.callback_query_handler(lambda callback_data: callback_data.data == 'startGPT')
async def start_GPT(callback_query: types.CallbackQuery):
    global gpt_generation_state
    if not gpt_generation_state:
        gpt_generation_state = True
        await callback_query.message.answer('GPT работает, спрашивай что тебе надо')
    else:
        gpt_generation_state = True
        await callback_query.message.answer('GPT заработал')

@dp.callback_query_handler(lambda callback_data: callback_data.data == 'stopGPT')
async def stop_GPT(callback_query: types.CallbackQuery):
    global gpt_generation_state
    if gpt_generation_state:
        gpt_generation_state = False
        await callback_query.message.answer('GPT не работает')
    else:
        gpt_generation_state = False
        await callback_query.message.answer('Генерация картинок перестала работать')

@dp.message_handler()
async def generate_message(message: types.Message):
    if gpt_generation_state == True:
        response_text = generate_text(message.text)
        await message.answer(response_text, reply_markup=get_GPT_stop())
    else:
        await message.answer('Запусти GPT')
@dp.message_handler()
async def handler_message(message: types.Message):
    user_text = message.text
    await message.answer('Идёт генерация изображения')

    try:
        if picture_generation_state == True:
            image_data = generate_image(user_text)
            await message.reply_photo(photo=image_data, reply_markup= get_picture_stop())
        else:
            await message.answer('Запусти генерацию картинок')
    except Exception as e:
        await message.answer(f'Произошла ошибка {e}')




async def on_startup(dispatcher):
    await set_comands(dispatcher.bot)

#конструкция для запуска бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

