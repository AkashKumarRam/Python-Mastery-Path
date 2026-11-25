marks = {
    "science": 99,
    "maths": 100,
    "computer": 98,
    "hindi": 78,
    "history": 91,
}

"""
items() = ei method ta akta list er bhetore key and value both return kore -

answer = marks.items()
print(answer)
"""

for sub, mark in marks.items():
    print(f"Subject is = {sub} and marks is = {mark}")
