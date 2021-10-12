import random


def unique(lst1: list, lst2: list) -> list:
    ans = []
    for i in lst1:
        if i in lst2:
            ans.append(i)
            del lst2[lst2.index(i)]

    return ans


if __name__ == '__main__':
    lst = [random.randint(0, 10) for _ in range(10)]
    lst1 = [random.randint(0, 10) for _ in range(10)]
    print(lst, lst1, sep="\n")
    print(unique(lst, lst1))
