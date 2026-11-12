marks = int(input("Enter Your Marks = "))

if marks >= 90 and marks <= 100:
    print("Your Grade is - A")
elif marks >= 80 and marks <= 89:
    print("Your Grade is - B")
elif marks >= 70 and marks <= 79:
    print("Your Grade is - C")
elif marks >= 60 and marks <= 69:
    print("Your Grade is - D")
elif marks >= 0 and marks <= 59: 
    print("You are Failed")
else:
    print("You are typed Invalid Number")