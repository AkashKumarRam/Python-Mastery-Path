student = {
    "name": "Akash",
    "age": 27,
}

# Same list e update, add perform hoi.
print(student, id(student))

# Update
student["age"] = 30

# Add
student["Gender"] = "Male"

# If you add multiple value in a list
student.update(
    {
        "City": "Jhargram",
        "Phone": 9903300678,
        "State": "West Bengal",
        "age": 28,
    }
)

print(student, id(student))
