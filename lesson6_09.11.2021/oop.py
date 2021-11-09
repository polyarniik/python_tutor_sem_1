"""
class - шаблон какой-либо сущности или предмета
экземпляр - объект, который принял скелет класса
метод - функция класса
поля, свойства класса - какие-либо свойства, которыми описывается класс

self - это значение, которое передаётся в каждом нестатическом методе,
оно хранит в себе название объекта, с которым дальше мы будем работать
"""


class Animal(object):

    def __init__(self, height: int, sound: str = "", is_can_fly: bool = False):
        self.sound = sound
        self.height = height
        self.is_can_fly = is_can_fly
        self.__notify_about_init()
        self.__set_sound_len()

    def __notify_about_init(self):
        print("Инициализирован")

    def get_my_attr(self):
        print(self.__sound_len)

    def __set_sound_len(self):
        self.__sound_len = len(self.sound)

    def make_sound(self):
        if self.sound:
            print(self.sound)
        else:
            raise ValueError("Это животное не может издавать звуки")

    def move_back(self):
        print(type(self))
        print("Переместились назад")

    def move_forward(self):
        print("Переместились вперёд")

    def __del__(self):
        print("Удалён")


cat = Animal(50, "Мяу", True)
dog = Animal(50, "Гав", True)
fish = Animal(100)
# b = Animal(1)
# c = Animal(1)
cat.get_my_attr()
cat.move_back()
cat.move_forward()
cat.make_sound()
dog.make_sound()

# dog.__notify_about_init()
dog._Animal__notify_about_init()

print(cat.height, cat.is_can_fly)


# print(a.height, a.is_can_fly, a.count_of_objects)
# print(c.height, c.is_can_fly, c.count_of_objects)
# print(c.height, c.is_can_fly, c.count_of_objects)

class B:
    pass
