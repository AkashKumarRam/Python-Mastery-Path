'''
Take numbers as input from the user one by one. Skip negative numbers
and keep adding the positive ones. Stop when the user enters 0 and print
the total. (Uses both continue and break.)
'''

total = 0

while True:
    numbers = int(input("Enter your number = "))
    if numbers == 0:
        break
    if numbers < 0:
        continue
    total = total + numbers
print(total)