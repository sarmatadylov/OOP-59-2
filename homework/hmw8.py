import sqlite3

# Подключение к базе данных
connect = sqlite3.connect("user_grades.db")
cursor = connect.cursor()

# Создание таблицы пользователей
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Создание таблицы оценок
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

connect.commit()

# Добавим примерные данные
cursor.executemany("INSERT INTO users(name, age) VALUES (?, ?)", [
    ("Алия", 18),
    ("Марат", 20),
    ("Жанна", 19)
])

cursor.executemany("INSERT INTO grades(user_id, subject, grade) VALUES (?, ?, ?)", [
    (1, "Математика", 90),
    (1, "История", 89),
    (1, "Биология", 80),
    (2, "Математика", 76),
    (2, "Физика", 70),
    (2, "История", 82)
])

connect.commit()

# Удаляем старое представление, если оно есть
cursor.execute("DROP VIEW IF EXISTS user_summary")

# Создаём представление (VIEW)
cursor.execute("""
CREATE VIEW user_summary AS
SELECT 
    u.name AS user_name,
    u.age AS age,
    ROUND(AVG(g.grade), 2) AS avg_grade,
    COUNT(g.subject) AS subjects_count
FROM users u
LEFT JOIN grades g ON u.id = g.user_id
GROUP BY u.id;
""")

connect.commit()
print(" Представление user_summary успешно создано!")

# Проверим содержимое представления
print("\n Сводная информация о пользователях:\n")
for row in cursor.execute("SELECT * FROM user_summary;"):
    print(row)

# Закрываем соединение
connect.close()
