import random

if __name__ == '__main__':
    lst = [random.randint(0, 10) for _ in range(50)]
    print(lst)
    ans = []
    for item in lst:
        if item not in ans:
            ans.append(item)
    print(ans)
    print(set(lst))

    for i in range(len(lst)):
        if len(lst) > i:
            if lst.count(lst[i]) > 1:
                del lst[i]

    print(lst)
