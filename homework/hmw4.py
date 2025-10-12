# Импортируем библиотеку
from faker import Faker

# Создаем объект Faker
fake = Faker()

# Генерируем и выводим случайное имя, адрес и email
print("Случайное имя:", fake.name())
print("Случайный адрес:", fake.address())
print("Случайный email:", fake.email())
