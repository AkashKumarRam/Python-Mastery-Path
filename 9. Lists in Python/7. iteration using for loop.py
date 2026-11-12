#       0.   1.  2.  3.  4.  5.  6
nums = [23, 43, 67, 54, 88, 12, 89]

"""
n = len(nums)
total = 0

for i in range(0, n):
    total = total + nums[i]
print(total, end=" ")
"""

# If you iterate value rather than index
"""
total = 0
for num in nums:
    total = total + num
print(total, end=" ")
"""


# Reverse iterate value
for num in nums[::-1]:
    print(num, end=" ")
