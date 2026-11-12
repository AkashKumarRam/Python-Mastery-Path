marks = [40, 76, 8, 99, 89, 37]

# To get the length
n = len(marks)
print(f"Length of List is = {n}")

# To get the Max
maxi = max(marks)
print(f"Maximum marks is = {maxi}")

# To get the Min
mini = min(marks)
print(f"Minimum marks is = {mini}")

# To get the Sum
total = sum(marks)
print(f"Total marks is = {total}")

# To Sort using sorted(), it will return you a new list (Accending Order)
new_list = sorted(marks)
print(f"Sorted list is = {new_list}")

# To Sort using sorted(), it will return you a new list (Decending Order)
new_list2 = sorted(marks, reverse=True)
print(f"Sorted list is = {new_list2}")

print(f"Our old list is remaining same = {marks}")
