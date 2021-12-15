import os
import shutil
from abc import ABC, abstractmethod


# class Command(ABC):
#
#     @abstractmethod
#     def execute(self, *args, **kwargs):
#         pass
#
#
# class ListFiles(Command):
#
#
#
# class ChangeDirectory(Command):
#
#     def execute(self, command, path):


def ls():
    count = 0
    for file in os.listdir():
        if count == 5:
            print()
        count += 1
        print(file, end=" ")
    print()


def cd(path: str):
    try:
        if path.strip() == "..":
            os.chdir(os.path.abspath(os.path.pardir))
        else:
            os.chdir(path)
    except FileNotFoundError:
        print("Такой директории нет")


def pwd():
    print(os.path.abspath(os.curdir))


def copy(src, dist):
    try:
        print(os.path.abspath(dist))
    except FileNotFoundError:
        print("Нет такого пути")

    shutil.copy(os.path.abspath(src), os.path.abspath(dist))
    print("Скопировано")


def move(src, dist):
    try:
        print(os.path.abspath(dist))
    except FileNotFoundError:
        print("Нет такого пути")

    shutil.move(os.path.abspath(src), os.path.abspath(dist))
    print("Перемещено")


def rm(path):
    os.remove(os.path.abspath(path))
    print("Удалено")
