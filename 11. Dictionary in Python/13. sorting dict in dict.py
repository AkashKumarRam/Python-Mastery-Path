students = {
    "Akash": {"math": 97, "physics": 94, "history": 91, "biology": 87, "english": 78},
    "Anjali": {"math": 87, "physics": 90, "history": 81, "biology": 67, "english": 98},
    "Subrata": {"math": 77, "physics": 99, "history": 92, "biology": 37, "english": 58},
    "Monu": {"math": 93, "physics": 44, "history": 51, "biology": 97, "english": 60},
    "Tonu": {"math": 37, "physics": 28, "history": 21, "biology": 67, "english": 70},
}

answer = dict(
    sorted(students.items(), key=lambda total: sum(total[1].values()), reverse=True)
)
print(answer)
