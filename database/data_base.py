import sqlite3

#инициализация базы данных
def initialize_db():
    conn = sqlite3.connect('bot_databaze.db')           #подключение к базе данных и называем её
    cursor = conn.cursor()                              #наш запрос, подключаемся к базе данных

    #создаём таблицу если она не создана, называем (users)
    #передаем id пользователя, тип данных - INTEGER (всегда должны что-то передаваться иначе не запишется)
    #к нему прирастим PRIMARY KEY  (ключ с помощью которого будем получать какую-то информацию)
    #создаём user_id, говорим что он всегда будет заполненым
    #username TEXT, first_name, TEXT last_name TEXT - текстовый формат
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    conn.commit()        #сохраняем что сделали
    conn.close()         #отсоединяемся, завершаем запрос




def add_user(user_id, username, first_name, last_name):
    conn = sqlite3.connect('bot_databaze.db')
    cursor = conn.cursor()

    #наш запрос
    #делаем выборку из таблицы users
    #VALUES (?, ?, ?, ?) - в этих местах мы обязаны что-то передать, а в

    cursor.execute('''
        INSERT INTO users (user_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name))
    conn.commit()
    conn.close()



def get_user(user_id):
    conn = sqlite3.connect('bot_databaze.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE user_id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user
