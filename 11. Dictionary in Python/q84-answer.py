"""
Populate a dictionary with six student names and their corresponding marks.
Loop through it and print the names of all students who achived a score
above 75.
"""

students = {
    "Akash": 100,
    "Anjali": 98,
    "Monu": 87,
    "Subrata": 74,
    "Tonu": 54,
    "Laxman": 96,
}

for name, mark in students.items():
    if mark >= 75:
        print(f"Student name is = {name} and Marks is = {mark}")
