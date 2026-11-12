'''
write a function that ask a number from user and prints if that number is odd
or even.
'''

def check_number():
    number = int(input("Enter Your Number = "))
    if number % 2 == 0:
        print("Your number is a Even number")
    else:
        print("Your number is a Odd number")

check_number()