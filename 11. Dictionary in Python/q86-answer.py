"""
Create a dictionary of 6 subjects and their respective marks. Print the
subject with the highest marks and the one with the lowest, using max()
and min() functions alogside with lambda expression.
"""

marks = {
    "Math": 97,
    "Physics": 94,
    "Biology": 87,
    "History": 91,
    "English": 78,
    "Geography": 89,
}

# print(
#     f"Maximum marks is = {max(marks.values())} and Minimum number is = {min(marks.values())}"
# )

maxi = max(marks.items(), key=lambda mark: mark[1])
print(maxi)

mini = min(marks.items(), key=lambda mark: mark[1])
print(mini)
