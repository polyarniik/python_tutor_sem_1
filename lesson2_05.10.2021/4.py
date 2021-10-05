from pprint import pprint

if __name__ == '__main__':
    N = int(input("Введите число: "))
    fibbonachi = [1, 1]

    while fibbonachi[-1] <= N:
        next_fibb = fibbonachi[-2] + fibbonachi[-1]
        if next_fibb <= N:
            fibbonachi.append(next_fibb)
        else:
            break

    pprint(fibbonachi)
