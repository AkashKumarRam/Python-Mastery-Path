'''
Write a function that print all the factors of a number entered by user.
'''

def check_factors():

    number = int(input("Enter Your Number = "))

    for i in range(1,number+1):
        if number % i == 0:
            print(f"Factors are = {i}")
             
check_factors()