def sum(num1,num2,num3):
    total = num1 + num2 + num3
    return total

answer = sum(20,30,90)
print(answer)

'''
True or false return, if user can vote or not
'''
def voting_criteria(age):
    if age >= 18:
        return print("User is eligable to Vote")
    else:
        return print("User is not eligable to Vote")

voter = voting_criteria(10)
