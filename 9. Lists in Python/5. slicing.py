#      0.  1.  2.  3.  4.  5.  6.   7    8.   9
#      -10 -9  -8 -7  -6  -5  -4  -3  -2    -1
lst = [23, 56, 74, 32, 67, 88, 63, 887, 226, 785]

lst1 = lst[0:4]
print(lst1)

lst2 = lst[3:9]
print(lst2)

# Black mane end tak automatic chole jabe
lst3 = lst[2:]
print(lst3)

# Stating theke given index porjonto jabe
lst4 = lst[:5]
print(lst4)

# Step Jumbing Slicing
lst5 = lst[0:9:2]
print(lst5)

# Reverse Slicing
lst6 = lst[8:1:-1]
print(lst6)
