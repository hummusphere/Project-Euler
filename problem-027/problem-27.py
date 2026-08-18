import math

possible_b_values = []
max_value = 1000
current_mult = 0
highest_prime_amount = 0

def find_possible_b_values(max_value):

    return_list = []

    for i in range(2, max_value+1):

        prime = True

        for k in range(2, math.ceil(math.sqrt(i))+1):

            if i%k == 0:

                prime = False

        if prime == True: 

            return_list.append(i)

    return return_list

possible_b_values = find_possible_b_values(max_value)

def check_prime(val):
    prime = True

    for k in range(2,math.ceil(math.sqrt(val))+1):

        if val%k == 0:

                prime = False

    return prime


def check_formulas(b, a):
    global highest_prime_amount
    global current_mult

    n = 0
    primes = []
    while True:
        formula_value = n**2 + (a*n) + b
        if formula_value < 2 or check_prime(formula_value) == False:

            if len(primes)>1 and len(primes) > highest_prime_amount:
                current_mult = a*b
                highest_prime_amount = len(primes)

            return 

        primes.append(formula_value)

        n+=1

for c in possible_b_values:

    for i in range(max_value*(-1), max_value+1):
        check_formulas(c, i)

print(current_mult)