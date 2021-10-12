import random


def minimum(lst: list) -> int:
    m = 101
    for i in lst:
        if m > i:
            m = i

    return m


def maximum(lst: list) -> int:
    m = -1
    for i in lst:
        if m < i:
            m = i

    return m


if __name__ == '__main__':
    # ListExspression || ListDefinition
    lst = [random.randint(0, 100) for _ in range(10)]
    # цикл ниже соответсвует выражению на 5 строке
    lst1 = []
    for i in range(10):
        lst1.append(random.randint(0, 100))

    print(lst)
    print(min(lst), minimum(lst))
    print(max(lst), maximum(lst))
