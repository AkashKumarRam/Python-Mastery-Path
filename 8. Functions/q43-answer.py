'''
Write a function called absolute_value that takes a number and returns
its absolute value without using the built-in abs() function.
'''

def absolute_value(number):
    if number >= 0:
        return number
    return number * -1

print(absolute_value(80))