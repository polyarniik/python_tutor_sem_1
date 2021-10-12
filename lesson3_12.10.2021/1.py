def multiply(lst: list) -> int:
    p = 1
    for i in lst:
        p *= i  # p = p * i

    return p


def summary(lst: list) -> int:
    sum = 0
    for i in lst:
        sum += i  # sum = sum + i

    return sum


if __name__ == '__main__':
    # lst = [1, 4, 4, 54, 64, 35, 65, 75, 92, 345]
    lst = [1, 2, 3, 4, 5, 6, ]
    print(multiply(lst))
    print(summary(lst))
