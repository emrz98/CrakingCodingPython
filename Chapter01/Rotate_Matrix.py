def rotate_matrix(matriz: list) -> list:
    ans = [
        [0 for j in range(len(matriz[i]))]
        for i in range(len(matriz))
    ]

    print(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ans[i][j] = matriz[j][len(matriz) - i - 1]
    print(ans)
    return ans
