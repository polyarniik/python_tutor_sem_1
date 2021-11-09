class Animal:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def take_breath(self):
        print("Сделать вздох")


class Tree:
    pass


class Mammal(Animal):

    def take_o2(self):
        print("Вздохнуть кислород")


class Dog(Mammal):
    is_pet = True

    def __init__(self, weight, height, name):
        super(Dog, self).__init__(weight, height)
        self.name = name

    def take_breath(self):
        # super(Dog, self).take_breath()
        print("Вздохнула собака")

    def run(self):
        print("Собака побежала")


fish = Animal(100, 35)
tiger = Mammal(200, 400)
dog = Dog(60, 40, "Шарик")
fish.take_breath()
tiger.take_breath()
tiger.take_o2()
dog.run()
dog.take_breath()
dog.take_o2()
print(vars(dog))
print(type(fish), type(tiger), isinstance(tiger, Animal), isinstance(fish, Mammal))

print("*" * 50)


class Monitor:
    height: int
    length: int
    quality: int

    def __init__(self, height, length, quality):
        self.height = height
        self.length = length
        self.quality = quality

    def show_monitor_quality(self):
        print(self.quality)

    def on(self):
        print("Монитор включён")

    def off(self):
        print("Монитор выключен")


class Keyboard:
    number_of_keys: int
    language: str

    def __init__(self, number_of_keys, language):
        self.number_of_keys = number_of_keys
        self.language = language

    def tap_to_key(self, key_name):
        print(f"Была нажата кнопка {key_name}")

    def on(self):
        print("Клавиатура включёна")

    def off(self):
        print("Клавиатура выключена")


class Notebook(Keyboard, Monitor):

    def __init__(self, number_of_keys, language, height, length, quality):
        super(Notebook, self).__init__(number_of_keys, language)
        Monitor.__init__(self, height, length, quality)

    def on_keyboard(self):
        Keyboard.on(self)

    def off_keyboard(self):
        Keyboard.off(self)

    def on(self):
        Monitor.on(self)

    def off(self):
        Monitor.off(self)

    def close_notebook(self):
        print("Закрыть ноутбук")


notebook = Notebook(70, "EN", 25, 30, 1080)
notebook.on()
notebook.off()
notebook.close_notebook()

print(isinstance(notebook, Monitor), isinstance(notebook, Keyboard))
# notebook.show_monitor_quality()
