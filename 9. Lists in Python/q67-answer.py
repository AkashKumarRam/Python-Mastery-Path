"""
Given a list of marks, use list comprehension to create a new list that
contains only the marks that are above 75.
"""

marks_list = [45, 67, 89, 28, 100, 90, 76]

new_list = [num for num in marks_list if num >= 75]
print(new_list)
