'''

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''

def zero_matrix(matrix):
    new_matrix = matrix.copy()
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    for r in row:
        for c in range(len(new_matrix[0])):
            new_matrix[r][c] =0
    for c in col:
        for r in range(len(new_matrix)):
            new_matrix[r][c] = 0
    return new_matrix

print(zero_matrix([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ]))
print(zero_matrix([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]))