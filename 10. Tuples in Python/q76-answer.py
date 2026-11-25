"""
Create a tuple of marks of 6 students. Print the highest, lowest, total
and average.
"""

marks = (45, 67, 98, 99, 76, 56)

n = len(marks)
total = sum(marks)

print(f"Highest marks is = {max(marks)} and Lowest marks is = {min(marks)}")
print(f"Total marks is = {total} and Average marks is = {total/n:.2f}")
