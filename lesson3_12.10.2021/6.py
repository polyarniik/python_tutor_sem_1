if __name__ == '__main__':
    lst = [1, 3, 4, 6, 6, 7, 8, 8, 9]

    lst1 = lst

    lst[1] = "trjkfjg"
    print(lst, lst1, sep="\n")

    # with copy
    print("*" * 10)
    lst = [1, 3, 4, 6, 6, 7, 8, 8, 9]

    lst1 = lst.copy()

    lst[1] = "trjkfjg"
    print(lst, lst1, sep="\n")
