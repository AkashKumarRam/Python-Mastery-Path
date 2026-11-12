'''
Take the user's age as input. Check and print whether they are eligable
to vote ( age >= 18 ) and whether they are senior citizen ( age >= 60 ).
print both result.
'''

age = int(input("Enter Your age = "))

print(f"Vote Eligiblity = {age >= 18} and senior Citizen = {age >= 60}")