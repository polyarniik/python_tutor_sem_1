from contextlib import suppress


def divide(a: int, b: int):
    try:
        return a / b
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except TypeError:
        if isinstance(a, str) and a.isdigit():
            a = int(a)
        elif isinstance(b, str) and b.isdigit():
            b = int(b)
        else:
            return "Введенные значения должны быть числами!"
        return divide(a, b)
    finally:
        print("Готово")


print(divide("1", "4"))


class ListLengthError(Exception):
    pass


def swap_list_items(lst: list):
    if len(lst) < 2:
        raise ListLengthError

    return [lst[-1], lst[0]]


with suppress(ZeroDivisionError):
    9 / 0

# if __name__ == '__main__':
#     try:
#         print(swap_list_items([1, 3]))
#         print(swap_list_items([[1, 2], [5, 6]]))
#         print(swap_list_items([]))
#     except ListLengthError:
#         print("Длина листа должна быть больше двух!")
