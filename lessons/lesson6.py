
#                  def say_hello 2 - ШАГ
def simple_decorator(func):
    def wrapper():
        print("До выполнения!!") # - 3 ШАГ
        func()      #   - 4 шаг
        print("До выполнения!!")    # - 5 ШАГ
    return wrapper
# simple_decorator(say_hello) 1 - ШАГ
@simple_decorator
def say_hello():
    print('Hello')

#say_hello()

def greeting_decorator(func):
    def wrapper(name):
        func(name)
        print(f"{name} как дела ?")
    return wrapper

@greeting_decorator
def greeting(name):
    print(f"{name} привет")

greeting("Ardager") # - 1 ШАГ greeting_decorator(greeting())
                      # def wrapper("Ardager")
def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat_decorator(4)
def say_name(name):
    print(f"{name}")

say_name("Ardager") # - repeat_decaorator(4)
                      # def decorator(def say_name())
                        # def wapper("Ardager")
                           # for i in range(4):
                            # say_name()

def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return "Я новый метод!!"
    return NewClass

class OldClass:

    def old_method(self):
        return "я старый метод!!"

obj_1 = OldClass()






class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def is_admin(func):
    def wrapper(user, command):
        if user.role == "admin" and command == "ban":
            func()
        else:
            print("Вы не админ или такой командый нет !!")
    return wrapper
@is_admin
def ban(user, command):
    print('Выполнен бан')

ban("Ardager", "bans")


def find_element(array, target):
    # print(array[target])
    for num, ind in enumerate(array):
        if target == ind:
            print('нашел')
        else:
            print("не нашел")
find_element([1,23,4,5,5,64,7,3], 3)


def find_element(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"LEFT: {left} == RIGHT: {right}")
        if array[mid] == target:
            return print("Найден")
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print("не найден!!")

    #for i in array:
     #   if i == target:
     #       print('нашли!!')
      #  else:
       #     print("Не нашли!!")

find_element([1,2,3,4,5,6,7,8,9,10,11], 11)