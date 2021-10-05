if __name__ == '__main__':
    MAX = int(input("Enter max number: "))
    # следующий цикл можно заменить ListDefinition: all_numbers = [i for i in range(2, MAX + 1)]
    all_numbers = []
    # for i in range(2, MAX + 1):
    #     all_numbers.append(i)
    #
    # for i in all_numbers:
    #     flag = True
    #     for j in range(2, i):
    #         if i % j == 0:
    #             flag = False
    #             all_numbers.remove(j)
    #             break
    #     if flag:
    #         for j in all_numbers:
    #             if j % i == 0 and i != j:
    #                 all_numbers.remove(j)

    for i in range(2, MAX + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            all_numbers.append(i)

    print(all_numbers)

    current = -1
    while True:
        inputs = input().split()

        command = inputs[0]
        step = 1
        if len(inputs) == 2:
            step = int(inputs[1])
            if step <= 0:
                print('Wrong input')
                continue
        elif len(inputs) > 2:
            print('Wrong input')
            continue

        if command == "next":
            current += step
            if current >= len(all_numbers):
                print("Numbers end")
                exit()
            print("Next number: ", all_numbers[current])
        elif command == "end":
            print("End of numbers")
            exit()
        else:
            print('Wrong input')
