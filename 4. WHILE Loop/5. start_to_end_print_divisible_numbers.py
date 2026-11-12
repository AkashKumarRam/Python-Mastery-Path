# print start to end, numbers which are divisible by 3 and 4

start = int(input("Enter your Starting Number = "))
end = int(input("Enter your Ending Number = "))

i = start

while i <= end:
    if i%3 == 0 and i%4 == 0:
        print(f"Your divisable numbers are = {i}")
    i += 1