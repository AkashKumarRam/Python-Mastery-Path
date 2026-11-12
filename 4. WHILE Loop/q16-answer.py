# Sum of all numbers from 1 to 100

start = int(input("Enter your staring number = "))
end = int(input("Enter your ending number = "))

i = start
total = 0

while i <= end:
    total = total + i
    i += 1
print(f"Your total is = {total}")