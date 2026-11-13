"""
Given a list of numbers, use a loop to calculate and print their average.
You can use len() to get count of elements, but avoid using sum() for the
total.
"""

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]


def sum_element(nums):
    n = len(nums)
    total = 0
    for num in nums:
        total = total + num
    average = total / n
    return f"Your average number is = {average:.2f}"


answer = sum_element(nums)
print(answer)
