class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025
        age = current_year - birth_year
        return cls(name, age)

person1 = Person("Алиса", 25)
print(person1.info)

print(Person.is_adult(20))
print(Person.is_adult(15))

person2 = Person.from_birth_year("Боб", 1999)
print(person2.info)
