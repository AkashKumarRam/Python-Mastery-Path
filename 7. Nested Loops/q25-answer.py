'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

number = int(input("Enter how many rows you want = "))

for i in range(1,number+1):
    for j in range(number, i-1, -1 ):
        print(j, end=" ")
    print() 
# for i in range(1,6):
#     for j in range(5, i-1, -1 ):
#         print(j, end=" ")
#     print() 