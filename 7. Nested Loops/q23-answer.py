'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
num = int(input("Enter Your number of lines = "))
for i in range(1,num+1):
    for j in range(i, 0, -1):
        print(j,end=" ")
    print()