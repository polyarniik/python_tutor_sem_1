if __name__ == '__main__':
    try:
        N = int(input())
        raise IOError
    except ValueError:
        print("Введено нечисловое значение.")
        exit()

    primes = []
    for i in range(2, N + 1):
        if N % i == 0:
            print(i)
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                primes.append(i)
    print(primes)
