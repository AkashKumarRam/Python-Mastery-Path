"""
Given a list, remove all dupllicate elements while preserving the original
order of the unique items.
"""

nums = [1, 3, 5, 6, 6, 8, 9, 1, 4, 3]


def remove_duplicates(nums):
    new_list = []

    for num in nums:
        if num not in new_list:
            new_list.append(num)

    return f"New List is = {new_list}"


answer = remove_duplicates(nums)
print(answer)
