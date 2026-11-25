student = {
    "name": "Akash",
    "age": 28,
    "Gender": "Male",
    "City": "Jhargram",
    "Phone": 9903300678,
    "State": "West Bengal",
}

print(student, id(student))

# To Delete a Value using Pop()
student.pop("State")

# To Delete all key and values in dictionary
# student.clear()

# To Delete entire variable | eta sudhu dictionary te noi sob jaigai use hoi
# del student

#  To Delete specific value using del function
del student["Phone"]

print(student, id(student))
