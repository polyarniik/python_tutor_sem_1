if __name__ == '__main__':
    words = ["fsdjkfs", "fdklf", "fdkfld", "ara", "a", "bbb", "erkgsllifvc"]
    ans = []

    for word in words:
        # if len(word) >= 3 and len(ans) <= 7:
        if 3 <= len(word) <= 7 and word[0] == word[-1]:
            ans.append(word)

    print(ans)
