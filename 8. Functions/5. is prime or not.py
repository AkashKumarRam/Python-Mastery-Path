# Return true if it is a prime number or retun false

def check_prime(number):
    count = 0
    
    for i in range(1,number+1):
        if number%i == 0:
            count += 1

    if count == 2:
        return True
    
    return False

print(check_prime(5))