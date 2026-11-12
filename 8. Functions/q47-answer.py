'''
Write a function power(base,exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
'''

# With using pow() inbuilt function
# def power(base,exp):
#     answer = pow(base,exp)
#     return answer

# print(power(3,3))

def power(base,exp):
    total = 1
    for i in range(1,exp+1):
        total = total * base
    return total

print(power(2,3))