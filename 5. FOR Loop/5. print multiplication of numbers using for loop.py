#  Ask a number from the user, print the multiplication table upto 10.

number = int(input("Enter Your Number = "))


for i in range( 1, 10 + 1):
    print(f"{number} x {i} = {number*i}")