"""
Create a 3X3 matrix (a nested list) and then use nested loops to calculate
and print the sum of all elements
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

total = 0
rows = len(matrix)
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        total = total + matrix[i][j]
print(f"Total sum of matrix is = {total}")
