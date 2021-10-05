if __name__ == '__main__':
    N = int(input())
    ans = ""
    while N != 0:
        ans += str(N % 2)
        N = N // 2

    print(ans[::-1])