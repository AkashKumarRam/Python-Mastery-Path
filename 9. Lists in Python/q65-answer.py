"""
Write a Python script that iterates through a list of integers and replaces
every negative numbers found in the list with the value of = 0.
"""

nums = [1, 3, 56, -78, 94, -32, 1, 5, 6, -7, -1]


def replace_value(nums):

    n = len(nums)

    for i in range(0, n):
        if nums[i] < 0:
            nums[i] = 0

    return f"Your replaced List is = {nums}"


answer = replace_value(nums)
print(answer)
