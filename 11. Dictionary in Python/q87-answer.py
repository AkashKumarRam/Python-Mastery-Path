"""
Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print
the full details of each student in a clear, readable format.
"""

students = {
    101: {"name": "Akash", "age": 27, "city": "Jhargram"},
    102: {"name": "Anjali", "age": 27, "city": "Kolkata"},
    103: {"name": "Tonu", "age": 29, "city": "Howrah"},
    104: {"name": "Monu", "age": 30, "city": "Jalpaiguri"},
}

for key, value in students.items():
    print(
        f"Roll no = {key}, Student info = {value['name']} | {value['age']} | {value['city']}"
    )
