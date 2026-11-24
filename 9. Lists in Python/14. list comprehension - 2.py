# Print 1 to 20 only Even numbers

even = [i for i in range(1, 21) if i % 2 == 0]
print(even)


# From 1 to 100, make a list of all Prime numbers.
def is_prime(num):
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors = factors + 1
    if factors == 2:
        return True
    return False


new_list = [i for i in range(2, 101) if is_prime(i) == True]
print(new_list)
