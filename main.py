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
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline_1, get_keyboard_inline_2, get_keyboard_inline_3, get_keyboard_inline_ege, get_keyboard_inline_not_url1
from database.data_base import initialize_db, add_user, get_user
from picture_bot import generate_image



bot = Bot(token=TELEGRAM_TOKEN)     #токен бота=нашему токену
dp = Dispatcher(bot)  #означает что бот будет соответствовать всем правилам

initialize_db()     #запустили базу данных

#как человек нажал команду старт, то мы создаем переменную user
#и с помощью get_user будем заносить нашу информацию из from_user.id
#и
#после команды старт загружается функциональность маркап клавиатур
@dp.message_handler(commands='start')           #обращениие к телеге
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я твой первый бот', reply_markup=get_keyboard_1(), reply=generate_image())
    else:
        await message.answer('Привет, я твой первый бот', reply_markup=get_keyboard_1())



#Генерация изображения
@dp.message_handler()
async def handler_message(message: types.Message):
    user_text = message.text
    await message.reply('Идёт генерация изображения')

    try:
        image_data = generate_image(user_text)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f'Произошла ошибка {e}')






#после нажатия на команду егэ
# загружается инлайн клавиатура с ссылками, добавляется фото
@dp.message_handler(commands='ege')
async def ege(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://kabinet-lichnyj.ru/wp-content/uploads/2021/05/1-58.jpg', caption='Я помогу тебе с ЕГЭ', reply_markup=get_keyboard_inline_ege())


#после нажатия на команду random_number
#загружается инлайн клавиатура, при нажатии на которую выдается рандомное число
@dp.message_handler(commands='random_number')
async def random_number(message: types.Message):
    await message.answer('Генерация рандомных чисел от 1 до 100', reply_markup=get_keyboard_inline_not_url1())

@dp.callback_query_handler(lambda c: c.data == 'send_random_number')    #lambda - функция сравнения
async def send_random_number(callback_query: types.CallbackQuery):
    send_random_num = random.randint(1, 100)
    await callback_query.message.answer(f'Ваше случайное число: {send_random_num}')






#создание маркап (в меню около ввода сообщения) клавиатур
#с добавлением инлайн (под сообщениями бота) клавиатур
@dp.message_handler(lambda message: message.text == 'Отправь фото дерзко')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0f2-ZM3WhR6_4njJXW4f2c9jlRemq449ruA&s', caption='Вот тебе сладенький)))', reply_markup=get_keyboard_inline_2())


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Попроси меня о чем-нибудь', reply_markup=get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Отправь фото природы')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://criterium.ru/wp-content/uploads/image.psd-38.webp', caption='Оки:)')


@dp.message_handler(lambda message:message.text == 'Отправь фото арнольда')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.sportvokrug.ru/f/1/statyi_o_sporte/arnold-schwarzenegger/Schwarzenegger3.png', caption='В зал быстро!', reply_markup=get_keyboard_inline_1())

@dp.message_handler(lambda message:message.text == 'Вернуться на первую клавиатуру')
async def button_5_click(message: types.Message):
    await message.answer('Тут ты можешь попросить меня о чём-нибудь', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Расскажи анекдот')
async def button_3_1_click(message: types.Message):
    await message.answer('— Будешь выходить — труп вынеси!'
'— Может быть, мусор?'
'— Может — мусор, может — сантехник, бог его знает…')


@dp.message_handler(lambda message: message.text == 'Вернуться на первую клавиатуру')
async def button_5_click(message: types.Message):
    await message.answer('Тут ты можешь попросить меня о чём-нибудь', reply_markup=get_keyboard_1())


@dp.message_handler(lambda message: message.text == 'Отправь фото macana')
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJEX2doGpvu5txyQl8-Uobo6v8RYwfcdKJ4w&s', reply_markup=get_keyboard_inline_3())



#кастомное меню (со всеми командами)
async def set_comands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для запуска бота'),
        types.BotCommand(command='/random_number', description='Случайное число...'),
        types.BotCommand(command='/ege', description='Ссылки на решу егэ')
    ]
    await bot.set_my_commands(commands)



async def on_startup(dispatcher):
    await set_comands(dispatcher.bot)


#конструкция для запуска бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




