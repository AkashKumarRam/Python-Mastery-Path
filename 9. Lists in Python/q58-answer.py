"""
Find the largest and smallest number in a list without using built-in
function like max() and min()
"""

nums = [4, 10, 45, 3, 16, 89, 56, 34, 21]


def find_number(nums):

    maxi = float("-inf")
    mini = float("inf")

    for num in nums:
        if num < mini:
            mini = num

    for num in nums:
        if num > maxi:
            maxi = num

    return f"Your Largest number is = {maxi} and Smallest number is = {mini}"


answer = find_number(nums)
print(answer)
