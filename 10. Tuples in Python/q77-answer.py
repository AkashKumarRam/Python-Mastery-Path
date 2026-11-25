"""
Take 5 numbers as input from the user, store them in a tuple, and print
the tuple along with its minimum and maximum.
"""

num1 = int(input("Enter Your first number = "))
num2 = int(input("Enter Your second number = "))
num3 = int(input("Enter Your third number = "))
num4 = int(input("Enter Your fourth number = "))
num5 = int(input("Enter Your fifth number = "))

nums = num1, num2, num3, num4, num5

maxi = max(nums)
mini = min(nums)

print(
    f"Your tuple is = {nums}, Maximum value is = {maxi} and Minimum value is = {mini}"
)
