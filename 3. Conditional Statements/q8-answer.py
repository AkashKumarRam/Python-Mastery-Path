'''
Take two numbers as input. Print the greater of two. If they are equal,
print "Both are equal"
'''

num1 = int(input("Enter Your First Number = "))
num2 = int(input("Enter Your Second Number = "))

if num1 > num2:
    print(f"Your first number is greater = {num1}")
elif num1 < num2:
    print(f"Your second number is greater = {num2}")
else:
    print("Both are equal")