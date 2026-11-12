# Print the numbers whuch are divisible by 3 and 5, from 1 to 100

# for i in range(1, 100+1):
#     if i%3 == 0 and i%5 == 0:
#         print(i,end=" ")

start = int(input("Enter your starting number = "))
end = int(input("Enter your ending number = "))

for i in range(start, end+1):
    if i%3 == 0 and i%5 == 0:
        print(i,end=" ")