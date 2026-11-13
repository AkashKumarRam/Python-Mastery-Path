"""
Write a program that takes a list and a target number. Use a loop to
determine if the target number exists in the list. Do not use the in
operator
"""

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]


def check_exists(targeted_number, nums):
    for num in nums:
        if targeted_number == num:
            return True

    return False


answer = check_exists(49, nums)
print(answer)
