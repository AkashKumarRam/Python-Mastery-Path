# Make a function which return min and max of list

nums = [1, 89, 3, 200, 876, 345, 31]


def min_max(nums):
    maxi = max(nums)
    mini = min(nums)

    return maxi, mini


ans1, ans2 = min_max(nums)

print(f"Maximum Value is = {ans1} and Minimum Value is = {ans2}")
