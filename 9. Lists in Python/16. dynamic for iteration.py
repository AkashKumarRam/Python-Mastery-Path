# 4 X 5

matrix = [
    [1, 2, 3, 4, 5],
    [8, 30, 45, 13, 40],
    [12, 45, 63, 87, 2],
    [73, 54, 123, 56, 78],
]

# To calculate number of rows
rows = len(matrix)
# To calculate number of columns
columns = len(matrix[0])

for i in range(0, rows):
    for j in range(0, columns):
        print(matrix[i][j], end=" ")
    print()
