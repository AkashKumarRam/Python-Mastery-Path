'''
A shop gives discount based on purchase amount:
Above 5000 -> 20% discount
Above 2000 -> 10% discount
Above 1000 -> 5% discount
1000 0r below -> no discount
'''

purchase_amount = int(input("Enter your purchased amount = "))

if purchase_amount >= 5000:
    print(f"You got 20% Discount = {purchase_amount}")

elif purchase_amount >= 2000 and purchase_amount < 5000:
    print(f"You got 10% Discount = {purchase_amount}")

elif purchase_amount >= 1000 and purchase_amount < 2000:
    print(f"You got 5% Discount = {purchase_amount}")

elif purchase_amount < 1000 and purchase_amount > 0:
    print(f"You dont get any discount = {purchase_amount}")

else:
    print("You are entered invalid number")