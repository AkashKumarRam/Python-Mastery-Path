'''
3 int as a parameter, print the total
'''

def total(num1,num2,num3):

    sum = num1 + num2 + num3

    print(f"Total is = {sum}")

total(10,20,40)

'''
Ask a name,age, gender. Print all of them
'''
def information(name,age,gender):
    print(f"Name is = {name}, age is = {age} and gender is = {gender}")

name = input("Enter Your Name = ")
age = int(input("Enter Your Age = "))
gender = input("Enter Your Gender = ")

information(name,age,gender)