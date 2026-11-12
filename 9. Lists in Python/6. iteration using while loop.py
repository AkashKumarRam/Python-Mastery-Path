#       0.   1.  2.  3.  4.  5.  6
nums = [23, 43, 67, 54, 88, 12, 89]

n = len(nums)
"""
i = 0
count = 0
while i <= n - 1:
    if nums[i] % 2 == 0:
        count += 1
    i += 1

print(count, end=" ")
"""
# Backward iteration
i = n - 1
while i >= 0:
    print(nums[i], end=" ")
    i -= 1
