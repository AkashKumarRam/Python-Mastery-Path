"""
Define a dictionary with five subjects and their respective marks. Utilize
the get() method to try accessing a subject that is not in in the dictionary,
ensure it print "Not Available" as a default.
"""

marks = {
    "Math": 97,
    "Physics": 94,
    "Biology": 87,
    "History": 91,
    "English": 78,
}
answer = marks.get("Geography", "Not Available")
print(answer)
