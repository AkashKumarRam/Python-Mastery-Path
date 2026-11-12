'''
A student scored marks in 3 subjects. Take all three as a input,
canculate the total and average, and print using an f-string.
'''
math = int(input("Enter your Mathematics Number = "))
physics = int(input("Enter your Physics Number = "))
chemistry = int(input("Enter your Chemistry Number = "))

total = math+physics+chemistry
average = total/3

print(f"Your total number is = {total} and Your average number is = {average:.2f}")