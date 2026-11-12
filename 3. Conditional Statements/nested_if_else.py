age = int(input("Enter Your age = "))
certification = input("Tell me you have certication or not = ")

if age >= 18:
    print("You age eligable to apply this job")
    if certification == "True":
        print("You are selected in our job")
    else:
        print("You need Certificate to selected in our job")
else:
    print("You dont have age to apply in this job")