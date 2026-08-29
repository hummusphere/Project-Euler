import math

primes_list = []
target_prime_factors = 4

def is_prime(test_number):

    for factor in range(2, math.ceil(math.sqrt(test_number))+1):
        if test_number%factor == 0 and not factor == test_number:
            return False

    return True

streak = 0

for i in range(2, 1000000):

    if is_prime(i):
        primes_list.append(i)
        streak = 0
        continue

    check_factors = i
    current_prime = 0
    factors = []

    while not check_factors == 1:

        if check_factors%primes_list[current_prime] == 0:

            check_factors/=primes_list[current_prime]
            factors.append(primes_list[current_prime])

        else:

            current_prime+=1

        if current_prime == len(primes_list):
            streak = 0
            break

    if check_factors == 1 and len(set(factors)) == target_prime_factors:
        print(i, factors)
        streak += 1
    else: 
        streak = 0

    if streak == target_prime_factors: 
        print("FOUND")
        break