# Ask a number from the user, and print all the factors.

number = int(input("Enter your number = "))

i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1