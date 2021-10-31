def rotate_matrix(matriz: list) -> list:
    ans = [
        [0 for j in range(len(matriz[i]))]
        for i in range(len(matriz))
    ]

    printMatrix(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ans[j][i] = matriz[len(matriz) - i - 1][j]

    print()
    printMatrix(ans)
    return ans


def rotate_matrix_n2(matriz: list) -> list:
    n = len(matriz)

    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matriz[first][i]

            matriz[first][i] = matriz[last - offset][first]
            matriz[last - offset][first] = matriz[last][last - offset]
            matriz[last][last - offset] = matriz[i][last]
            matriz[i][last] = top

    return matriz


def printMatrix(matrix: list):
    for row in matrix:
        print(row)
