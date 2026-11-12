'''
Take a number as input. Using the ternary operator, print "Even" or "Odd"
in a single line.
'''

number = int(input("Enter Your Number = "))

final_number = "Even" if number%2 == 0 else "Odd"

print(final_number)