name = "Akash"
age = 26
cgpa = 9.7
is_student = False
gender = "Male"

print("Hello",name,"Your age is",age)
# print("Hello " + name + " Your gender is " + gender)
'''
This is Akash
I lived in Jhargram
'''
#seprator="sep" - er bhetore ja dibe seitai duto word er majhkhane asbe
print (name,age,gender,sep='lol')

#end = by default python er print statement new line theke start hoi kintu jodi chau new line er jaigai kichu dite tahole end statement dite paro
print(name,end=' ')
print(age,end=' ')
print(gender)

# F-String
print(f"My name is {name}, age is {age}, and gender is {gender}")