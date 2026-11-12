# start to end print even numbers

start = int(input("Enter your Starting Number = "))
end = int(input("Enter your Ending Number = "))

i = start

while i <= end:
    if i % 2 == 0:
        print(i)
    i += 1