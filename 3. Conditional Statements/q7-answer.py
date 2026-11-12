'''
Take a number as input. Print whether it is positive, negative or zero.
'''

num = int(input("Enter Your Number = "))

if num > 0:
    print(f"You are entered a positive number = {num}")
elif num < 0:
    print(f"You are entered a negative number = {num}")
else:
    print(f"You are entered Zero = {num}")