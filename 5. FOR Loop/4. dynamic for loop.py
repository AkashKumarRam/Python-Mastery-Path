start = int(input("Enter your starting number = "))
end = int(input("Enter your ending number = "))

total = 0

for i in range(start, end+1):
    total = total + i
print(f"Total is = {total}")