# Родительский класс
class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Транспорт движется со скоростью {self.speed} км/ч"


# Дочерний класс
class Car(Transport):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def move(self):
        return f"Машина {self.brand} едет со скоростью {self.speed} км/ч"


# Создание объекта класса Car
car = Car(120, "BMW")

# Вызов метода move()
print(car.move())
