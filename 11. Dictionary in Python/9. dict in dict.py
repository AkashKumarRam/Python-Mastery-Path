students = {
    "101": {
        "name": "Akash",
        "age": 27,
        "City": "Jhargram",
    },
    "102": {
        "name": "Anjali",
        "age": 26,
        "City": "Kolata",
    },
    "103": {
        "name": "Soumya",
        "age": 27,
        "City": "Bangalore",
        "details": {"Phone": 9903300678, "Home": "Midnaporee"},
    },
}

# How to access
print(students["101"])
print(students["102"]["age"])
print(students["103"]["details"]["Phone"])

total = 0

for roll_no, info in students.items():

    total += info["age"]

    print(
        f"Roll no is = {roll_no}, Student name is = {info['name']} and age is = {info['age']}"
    )
print(f"Total age of students is = {total}")
