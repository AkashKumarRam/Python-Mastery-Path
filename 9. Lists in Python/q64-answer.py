"""
Given a list of numbers (which may contain duplicates). Write a Python script
that takes an integer as input from the user and remove all occurrences of
that integers from the list.
"""

nums = [1, 2, 5, 6, 7, 4, 7, 8, 98, 67, 51, 23, 2, 5, 8, 1, 2, 2, 2, 2]


def remove_occurrences(nums):

    target_number = int(input("Enter Your number = "))

    # If you want to do in the same list without craeting new list
    while target_number in nums:
        nums.remove(target_number)
    return f"Your clean List is = {nums}"


'''
    Methord = 2 ( Using New List )
    new_list = []

    for num in nums:
        if num != target_number:
            new_list.append(num)

    return f"Your clean list is = {new_list}"'''


answer = remove_occurrences(nums)
print(answer)
