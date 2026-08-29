import math
prime_list = []

def is_prime(test_number: int):

    for factor in range(2, math.ceil(math.sqrt(test_number))+1):
        if test_number%factor == 0 and not factor == test_number:
            return False

    return True

def convert_to_list(num: int) -> list:

    return_list = []

    for letter in str(num):
        return_list.append(letter)

    return_list.sort()

    return return_list


for i in range(1000, 10000):
    if is_prime(i):
        prime_list.append(i)

for prime_index in range(0, len(prime_list)):

    permutations = []

    permutations.append(prime_list[prime_index])

    for second_prime_index in range(prime_index+1, len(prime_list)):

        if convert_to_list(prime_list[second_prime_index]) == convert_to_list(prime_list[prime_index]):

            permutations.append(prime_list[second_prime_index])

    if len(permutations) == 3 and permutations[1]-permutations[0] == permutations[2] - permutations[1]:
        print(str(permutations[0])+str(permutations[1])+str(permutations[2]))
