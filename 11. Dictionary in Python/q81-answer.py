"""
Construct a dictionary containing four product names and their prices.
Prompt the user to enter a product name. Use the "in" keyword to check
if it exists; if so, display its price. Otherwise, inform the user
"Product not found".
"""

products = {
    "Mobile": 70000,
    "TV": 600000,
    "AC": 50000,
    "Fridge": 30000,
}

product = input("Enter your product name = ")

if product in products:
    print(f"Product is = {product} and price is = {products[product]}")
else:
    print("Product not found")
