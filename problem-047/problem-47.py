import math
prime_list = []

def is_prime(test_number):

    for factor in range(2, math.ceil(math.sqrt(test_number))+1):
        if test_number%factor == 0:
            return False

    return True

def is_composite_odd(test_number):

    if test_number%2 == 0:
        return False

    if not is_prime(test_number):
        return True

    return False

for i in range(2, 1000000):

    if is_prime(i):
        prime_list.append(i)

    if not is_composite_odd(i):
        continue

    conjecture_true = False
    for prime in prime_list:    

        difference  = math.sqrt((i - prime)/2)

        if difference == math.ceil(difference):
            conjecture_true = True

    
    print(i, conjecture_true)
    if conjecture_true == False:
        break