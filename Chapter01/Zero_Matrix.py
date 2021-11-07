def make_matrix_zero(matrix: list) -> list:
    row_col = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_col.append((i, j))

    for temp in row_col:
        for i in range(len(matrix)):
            matrix[i][temp[1]] = 0
        for j in range(len(matrix[0])):
            matrix[temp[0]][j] = 0

    return matrix
