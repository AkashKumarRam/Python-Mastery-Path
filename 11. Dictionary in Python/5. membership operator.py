student = {
    "name": "Akash",
    "age": 28,
    "Gender": "Male",
    "City": "Jhargram",
}

# print("age" in student)

key = input("Enter Your Key = ")

if key in student:
    print(f"Your key value is = {student[key]}")
else:
    print("Your are entering wrogn key")
