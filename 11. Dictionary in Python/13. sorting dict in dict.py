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


"""
zip() method = deita list ke aksathe jora lagiye dei - 

names = ["Akash", "Anjali", "Rahul"]
marks = [97, 90, 92]

new_list = dict(zip(names, marks))
print(new_list)
"""


"""
Zip duto list er modhe jokhon zip kore tokhon choto list porjonto chole
tarpor stop hoye jai - 

names = ["Akash", "Anjali", "Rahul"]
marks = [97, 90]

new_list = dict(zip(names, marks))
print(new_list)
"""


"""
Zip same key but value alada thakle akta key pic kore last er value take
tule updated value dekhai - 

names = ["Akash", "Anjali", "Anjali"]
marks = [97, 90, 99]

new_list = dict(zip(names, marks))
print(new_list)
"""
