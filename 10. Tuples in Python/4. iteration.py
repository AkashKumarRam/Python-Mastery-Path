my_tuple = (1, 3, 4, 600, "Akash", "Subrata", "Anjali")

# Three type of iteration in Tuples

n = len(my_tuple)

# 1st Methord
for i in range(0, n):
    print(my_tuple[i], end=" ")
print()

# 2nd Methord
for element in my_tuple:
    print(element, end=" ")
print()

# 3rd Methord
for index, value in enumerate(my_tuple):
    print(f"Index is = {index} and Value is = {value}")

# Converting between List and Tuples
new_tuple = (1, 2, 4, 5, "Akash")
print(list(my_tuple))

new_list = [2, 4, "Anjali"]
print(tuple(new_list))


# Apply some methord in Tuples
nums = (1, 4, 5, 2, 78, 91, 12)

print(min(nums))
print(max(nums))
print(sum(nums))
print(sorted(nums))
