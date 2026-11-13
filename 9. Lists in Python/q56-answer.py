"""
Given two list of the same length, write Python code using a loop to create
a new list where each element is the sum of the corresponding elements from
both original list.
"""

num1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
num2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]


def sum_of_two_list(num1, num2):

    new_list = []
    n = len(num1)

    for i in range(0, n):

        total = num1[i] + num2[i]
        new_list.append(total)

    return f"Your new List is = {new_list}"


answer = sum_of_two_list(num1, num2)
print(answer)
