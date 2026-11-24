"""
Given a 4X4 matrix, print only the border elements and replace the inner
elements with an asterisk (*).

Expected Output =

1 2 3 4
5 * * 8
9 * * 12
13 14 15 16
"""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
