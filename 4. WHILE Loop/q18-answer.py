#  Ask a number from the user, print the multiplication table upto 10.

number = int(input("Enter Your Number = "))

i = 1

while i<=10:
    multi = number * i
    print(f"{number} X {i} = {multi}")
    i += 1

