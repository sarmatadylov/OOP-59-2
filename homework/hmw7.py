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
    print(" User added!")


# Функция чтения всех пользователей
def read_users():
    cursor.execute("SELECT rowid, * FROM users")
    users = cursor.fetchall()
    for i in users:
        print(f"ID: {i[0]} | NAME: {i[1]} | AGE: {i[2]} | HOBBY: {i[3]}")


#  Функция обновления пользователя
def update_user(rowid, name=None, age=None, hobby=None):
    # Список для хранения полей, которые нужно обновить
    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if hobby is not None:
        fields.append("hobby = ?")
        values.append(hobby)

    # Если ничего не передано — ничего не делаем
    if not fields:
        print(" Нет данных для обновления!")
        return

    # Добавляем ID в конец списка значений
    values.append(rowid)

    # Формируем SQL-запрос динамически
    sql = f"UPDATE users SET {', '.join(fields)} WHERE rowid = ?"
    cursor.execute(sql, values)
    connect.commit()
    print(f" User with ID {rowid} updated!")


#  Функция просмотра пользователя по ID
def read_user_by_id(rowid):
    cursor.execute("SELECT rowid, * FROM users WHERE rowid = ?", (rowid,))
    user = cursor.fetchone()
    if user:
        print(f"ID: {user[0]} | NAME: {user[1]} | AGE: {user[2]} | HOBBY: {user[3]}")
    else:
        print(" Пользователь не найден!")


# Пример использования
create_user('Sarmat', 19, 'Спать')
create_user('Nikita', 25, 'Играть в шахматы')
create_user('Alex', 30, 'Плавать')

print("\n Все пользователи:")
read_users()

print("\n Обновление пользователя:")
update_user(rowid=2, hobby="Читать книги")

print("\n Просмотр конкретного пользователя:")
read_user_by_id(2)

