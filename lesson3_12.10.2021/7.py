if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3],
        [5, 6, 7],
        [4, 9, 0],
    ]

    matrix2 = [
        [4, 7, 6],
        [5, 2, 7],
        [9, 3, 8],
    ]

    matrix3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

    # "динамическое" создание матрицы
    matrix4 = []
    for i in range(len(matrix1)):
        matrix4.append([])
        for j in range(len(matrix1)):
            matrix4[i].append(0)
            for k in range(len(matrix1)):
                matrix4[i][j] += matrix1[i][k] * matrix2[k][j]

    print(matrix4)
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            print(matrix3[i][j], end=" ")
        print()
