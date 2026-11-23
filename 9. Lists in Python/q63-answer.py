"""
Create a list containing the squares of numbers from 1 to 10
"""


def check_squares():

    lst = []

    for i in range(1, 11):

        square = i * i
        lst.append(square)

    return f"Square of List is = {lst}"


answer = check_squares()
print(answer)
