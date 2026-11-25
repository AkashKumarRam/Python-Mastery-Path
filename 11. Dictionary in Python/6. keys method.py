marks = {
    "science": 99,
    "maths": 100,
    "computer": 98,
    "hindi": 78,
    "history": 91,
}

"""
key() = methord er madhome amra dictionary er somosto keys jante pari
etate key er akta list return korbe -

key = marks.keys()
print(key)
"""

# Iteration using key
total = 0

for subject in marks.keys():
    print(f"Subjects are = {subject} and marks are = {marks[subject]}")
    total = total + marks[subject]
print(f"Your total marks is = {total}")
