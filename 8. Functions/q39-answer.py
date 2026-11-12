'''
Write a function called find_max that takes three numbers as parameters
and print the largest one
'''

def find_max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(f"Your largest number is = {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"Your largest number is = {num2}")
    elif num3 > num1 and num3 > num2:
        print(f"Your largest number is = {num3}")
    else:
        print("You are entered dublicate numbers")

find_max(20,80,97)