marks = {
    "Science": 99,
    "Maths": 100,
    "Computer": 98,
    "Hindi": 79,
    "History": 91,
}

# print(marks["Computer"])
"""
Jodi tumi chau je key jodi na paoa jai tahole custom message return korte
answer = marks.get("Geo", "Key doesnot exists")
print(answer)
"""

subject = str(input("Enter Your Subject = "))
answer = marks.get(subject)

if answer is None:
    print("Subject is not Found")
else:
    print(f"Marks Scored = {answer}")
