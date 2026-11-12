'''
Take three numbers as input. Print the largest of three without using
any built-in-function.
'''

num1 = int(input("Enter Your First Number = "))
num2 = int(input("Enter Your Second Number = "))
num3 = int(input("Enter Your Third Number = "))

if num1 > num2 and num1 > num3:
    print(f"Largest number is your First Number = {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Largest number is your Second Number = {num2}")
elif num3 > num1 and num3 > num2:
    print(f"Largest number is your Third Number = {num3}")
elif num1 == num2 and num1 > num3:
    print(F"Your first number and second number is bigges and equel")
elif num2 == num3 and num2 > num1:
    print(F"Your second number and third number is bigges and equel")
elif num3 == num1 and num3 > num2:
    print(F"Your first number and third number is bigges and equel")
else:
    print("Your numbers are equal")