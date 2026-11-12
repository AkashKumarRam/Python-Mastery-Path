'''
Write a function tax_calculator(income) that takes annual income and returns
the tax amount based on these slabs.

- Up to 250000 -> No tax
- 2500001 to 500000 -> 5%
- 5000001 to 1000000 -> 20%
- Above 1000000 -> 30%
'''

def tax_calculator(income):
    if income <= 250000:
        return f"You are not eligable to tax slabs = {income}"
    elif income >= 250001 and income <= 500000:
        return f"You are i the 5% Tax Slabs = {income}"
    elif income >= 500001 and income <= 1000000:
        return f"You are in the 20% Tax Slabs = {income}"
    else:
        return f"You are in the 30% Tax slabs = {income}"

answer = tax_calculator(5000)
print(answer)