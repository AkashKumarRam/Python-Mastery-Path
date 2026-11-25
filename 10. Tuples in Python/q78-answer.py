"""
Write a function get_stats(nums) that takes a tuple of numbers and returns
a tuple containing the sum, average, minimum and maximum.
Unpack the returned tuple and print each value.
"""

nums = (23, 89, 97, 45, 12, 56)


def get_stats(nums):

    n = len(nums)

    maxi = max(nums)
    mini = min(nums)
    total = sum(nums)
    average = total / n

    return maxi, mini, total, average


maxi, mini, total, average = get_stats(nums)

print(f"Maximum value is = {maxi}")
print(f"Minimum value is = {mini}")
print(f"Total value is = {total}")
print(f"Average value is = {average:.2f}")
