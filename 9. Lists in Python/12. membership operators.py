fruits = ["Apple", "Banana", "Kiwi", "Mango", "Dragon Fruit", "Orange"]

print("Apple" in fruits)
print("Coconut" in fruits)

print("Orange" not in fruits)
print("Lichi" not in fruits)


target = input("Enter Your Fruit name = ")

if target in fruits:
    fruits.remove(target)
    print(f"Your fruits buckets are = {fruits}")
else:
    print("Cannot remove target because target doesnot exists")
