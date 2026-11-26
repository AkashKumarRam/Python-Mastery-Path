"""
Create a dictionary for a student, including key like name, age, city and
marks (as list of scores ). Print each piece of information using its key.
"""

student = {
    "name": "Akash",
    "age": 27,
    "city": "Jhargram",
    "marks": [97, 94, 78, 91],
}

for info in student.keys():
    print(f"Keys are = {info} and Informations are = {student[info]}")
