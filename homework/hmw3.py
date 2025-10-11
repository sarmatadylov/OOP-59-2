class Car:
    def __init__(self, brand):
        self.brand = brand    # публичный атрибут
        self._fuel_level = 0  # защищенный атрибут
        self._engine_status = False  # приватный атрибут

    def start_engine(self):
        if self._fuel_level > 0:
            self._engine_status = True
            print("Двигатель запущен!")
        else:
            print("Невозможно завести двигатель - нет топлива! -_-")

    def stop_engine(self):
        self._engine_status = False
        print("Двигатель остановлен.")

    def _check_fuel(self, distance):
        """Приватный метод: проверяет, хватает ли топлива."""
        return self._fuel_level >= distance * 0.1

    def drive(self, distance):
        if not self._engine_status:
            print("Сначало нужно запустить двигатель!")
            return

        if self._check_fuel(distance):
            self._fuel_level -= distance * 0.1
            print(f"Проехали {distance} км, осталось {round(self._fuel_level, 1)} литров топлива.")
        else:
            print("Недостаточно топлива для поездки!")

    def refuel(self, amont):
        self._fuel_level += amont
        print(f"Заправлено {amont} литров. Текущий уровень топлива: {self._fuel_level} л.")

    def get_status(self):
        engine_state = "включен" if self._engine_status else "включен"
        return f"Марка: {self.brand} | Топливо: {round(self._fuel_level, 1)} | Двигатель: {engine_state}"

car = Car("Subaru")
car.refuel(20)
car.start_engine()
car.drive(60)
print(car.get_status())
