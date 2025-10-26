import sqlite3

# Подключение к базе данных
connect = sqlite3.connect("users.db")
cursor = connect.cursor()

# Создание таблицы
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
connect.commit()


# Функция добавления пользователя
def create_user(name, age, hobby):
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print("User added!")




# Функция чтения всех пользователей
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")



#create_user('Sarmat', 19, 'Спать')   # если хочешь добавить новых

read_users()






