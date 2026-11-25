marks = {
    "science": 99,
    "maths": 100,
    "computer": 98,
    "hindi": 78,
    "history": 91,
}

"""
values() = ei method diye value direct access korte parbo ar etau return kor
new list - 

value = marks.values()
print(f"Values are = {value}")
"""

total = 0

for mark in marks.values():
    total = total + mark
print(f"Your total marks is = {total}")
