"""
Create a Tuple of 8 numbers. Using slicing, print the first 3 and last 3
and every alternative element.
"""

nums = (1, 2, 3, 4, 5, 6, 7, 8)

print(f"First 3 number is = {nums[:3]}")
print(f"Last 3 number is = {nums[-3:]}")
print(f"Every alternative element is = {nums[::2]}")
