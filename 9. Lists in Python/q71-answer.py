"""
Given a 3X3 matrix, print only the main diagonal elements and replace
overthing else with an asterisk (*).

Expected Output =

1 * *
* 5 *
* * 9
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
