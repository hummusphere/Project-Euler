import math

max = 1000000
prime_list = [2]

def is_prime(test_number: int):

    for factor in range(2, math.ceil(math.sqrt(test_number))+1):
        if test_number%factor == 0:
            return False

    return True



for i in range(2, max):

    if not is_prime(i):
        continue

    prime_list.append(i)

highest_counter = 0
highest_consecutive = 0

for prime_index in range(0, len(prime_list)):

    sum = prime_list[prime_index]
    counter = 1

    for second_prime_index in range(prime_index+1, len(prime_list)):

        sum += prime_list[second_prime_index]
        counter+=1

        if counter > highest_counter and sum in set(prime_list):

            highest_consecutive = sum
            highest_counter = counter

        if sum > prime_list[len(prime_list)-1]:

            break

print(highest_consecutive)