"""
Given a dictionary of marks for different subjects. loop over its values()
to calculate and print the total marks and the average mark obtained.
"""

marks = {
    "Math": 97,
    "Physics": 94,
    "Biology": 87,
    "History": 91,
    "English": 78,
}

n = len(marks)
total = 0

# Etar sahajje dictionary er bhetorer values sum ber kore dite parbo
# total_marks = sum(marks.values())

for mark in marks.values():
    total = total + mark

average = total / n
print(f"Total marks is = {total} and average marks is = {average:.2f}")
