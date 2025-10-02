class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Город: {self.city}"


# создаём 2 экземпляра класса
person1 = Person("Алина", 25, "Алматы")
person2 = Person("Санжар", 30, "Бишкек")

# вызываем метод и выводим результат
print(person1.info())
print(person2.info())
