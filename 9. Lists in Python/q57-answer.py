"""
Write a program that takes a list of numbers and using a loop, determines
whether it is sorted in accending order, print True if it is sorted, and
False otherwise
"""

nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 68, 79, 100]


def check_sorted(nums):

    n = len(nums)

    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


answer = check_sorted(nums)
print(answer)
