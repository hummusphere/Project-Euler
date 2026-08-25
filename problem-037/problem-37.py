import math

primes = []
truncatable_primes = []
max = 1000000
sum = 0

def check_prime(number):
    if number == 1:
        return False

    for k in range(2, math.ceil(math.sqrt(number))+1):
        if number%k == 0 and not number == k:
            return False

    return True

for i in range(2, max):
    if check_prime(i) == True:
        if i > 10:
            primes.append(i)

for prime in primes:

    is_truncatable = True

    for i in range(0, 2):

        str_one = ''

        for letter in str(prime):

            if i == 1:
                str_one = letter + str_one
            else:
                str_one+=letter
                
            if not check_prime(int(str_one)):
                is_truncatable = False

        prime = str(prime)[::-1]

    if is_truncatable == True:
        truncatable_primes.append(int(prime))
        sum+= int(prime)

print(truncatable_primes)
print(sum)