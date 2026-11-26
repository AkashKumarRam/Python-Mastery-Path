marks = {
    "Math": 97,
    "Physics": 94,
    "Biology": 87,
    "History": 91,
    "English": 78,
}

# Sort using name of first letter
answer = dict(sorted(marks.items(), key=lambda num: num[0]))
print(answer)

# Sort using number
number = dict(sorted(marks.items(), key=lambda num: num[1]))
print(number)
