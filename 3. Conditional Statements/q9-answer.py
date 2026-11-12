'''
Take a student's marks as input. Print their grade based on this scale:
90 and Above -> A
75 to 89 -> B
60 to 74 -> C
40 to 59 -> D
Below 40 -> F
'''
marks = int(input("Enter Your Marks = "))

if marks >= 90 and marks <= 100: 
    print(f"Your Grade is = A {marks}")
elif marks >= 75 and marks <= 89:
    print(f"Your Grade is = B {marks}")
elif marks >= 60 and marks <= 74:
    print(f"Your Grade is - C {marks}")
elif marks >= 40 and marks <= 59:
    print(f"Your Grade is - D {marks}")
elif marks < 40 and marks >= 0:
    print(f"Your are Failed {marks}")
else:
    print("You are entered invalid number")