'''
Write a function fizzbuzz(n) that takes a single number and prints "Fizz"
if its divisible by 3, "Buzz" if its divisible by 5, "FizzBuzz" if it's 
divisible by both, otherwise print the number itself.
'''

def fizzbuzz(number):
    if number%3 == 0 and number%5 == 0:
        return print(f"FizzBuzz = {number}")
    elif number%5 == 0:
        return print(f"Buzz = {number}")
    elif number%3 == 0:
        return print(f"Fizz = {number}")
    else:
        return print(f"Number is = {number}")

print(fizzbuzz(9))