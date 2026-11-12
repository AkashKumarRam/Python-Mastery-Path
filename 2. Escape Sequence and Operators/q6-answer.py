'''
Take two number as input. Without using *, calculate and print their product
using += in a way that adds the first number to itself the second number
of times. (Think carefully)
'''

num1 = int(input("Enter Your First Number = "))
num2 = int(input("Enter Your Second Number = "))

total = 0

total += num1/(1/num2)
print(f"Final number is = {total}")