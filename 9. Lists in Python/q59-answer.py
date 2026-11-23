"""
Reverse a List without using .reverse() methord or List slicing ([::-1])
"""

nums = [1, 2, 3, 4, 5]


def reverse_list(nums):
    n = len(nums)
    new_list = []

    for i in range(n - 1, -1, -1):
        new_list.append(nums[i])

    return f"Revesrsed list is = {new_list}"


answer = reverse_list(nums)
print(answer)
