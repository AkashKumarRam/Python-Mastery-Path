"""
Given a 3x3 matrix, print only the anti-diagonal (top-right to bottom-left)
elements and replace everything else with an asterisk (*).

Expected output =

* * 3
* 5 *
7 * *
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
        if i + j == 2:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
