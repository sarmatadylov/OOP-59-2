class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def __add__(self, other):
        if self.author == other.author:
            return self.pages + other.pages
        else:
            return "Нельзя сложить книги разных авторов"

book1 = Book("Гарри Поттер и кубок огня", "Джоан Роулинг", 636)
book2 = Book("Плаха", "Чингиз Айтматов", 415)
book3 = Book("1984", "Джордж Оруэлл", 328)

print(book1)
print(book2)
print(book3)

print(book1 + book2)
print(book1 + book3)