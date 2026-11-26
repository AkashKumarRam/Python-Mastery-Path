marks = {
    "Akash": [97, 94, 91, 87, 78],
    "Anjali": [87, 90, 81, 67, 98],
    "Subrata": [77, 99, 92, 37, 58],
    "Monu": [93, 44, 51, 97, 60],
    "Tonu": [37, 28, 21, 67, 70],
}

answer = dict(sorted(marks.items(), key=lambda name: name[1][-1]))
print(answer)

# Sorting using total marks of a student
info = dict(sorted(marks.items(), key=lambda mark: sum(mark[1]), reverse=True))
print(info)
