"""
Separate a list of integers into two distinct lists: one contains all the
even numbers and other one contains all the odd numbers
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 54, 68, 90, 24, 53, 12]


def check_even_odd(nums):

    even_list = []
    odd_list = []

    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return f"Even List is = {even_list} and odd list is = {odd_list}"


answer = check_even_odd(nums)
print(answer)
