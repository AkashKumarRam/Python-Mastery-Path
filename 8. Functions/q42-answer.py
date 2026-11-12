'''
Write a function called min_of_three that takes three numbers and returns
the smallest without using built-in function.
'''

def min_of_three(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        return f"smallest number is = {num1}"
    elif num2 < num1 and num2 < num3:
        return f"smallest number is = {num2}"
    return f"smallest number is = {num3}"

answer = min_of_three(106,235,67)
print(answer)