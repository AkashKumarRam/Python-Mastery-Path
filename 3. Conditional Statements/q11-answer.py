'''
Take a person's age and whether they have a valid ID(True/False) as input.
They can enter a venue only if they are 18 or older AND have a valid ID.
print the appropriate message.
'''
age = int(input("Enter Your Age = "))
id_proof = input("You Have ID = ")

if age >= 18:
    print("Your age is eligable to attend venue")
    if(id_proof == "True"):
        print("You have entered our venue because you have id")
    else:
        print("You are not have entered our venue because you dont have id")
else:
    print("Your age is not eliagble to entered our venue")