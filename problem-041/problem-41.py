import math

max = 10000000
highest_pandigital = 0

def is_prime(num):

    for k in range(2, math.ceil(math.sqrt(num))+1):

        if num%k == 0:

            return False

    return True


for i in range(2, max):
    print(i)

    if not is_prime(i):
        continue

    num_list = []

    for k in str(i):

        num_list.append(int(k))

    num_list.sort()

    if len(num_list) != len(set(num_list)):
        continue

    is_pandigital = True

    for z in range(0,len(num_list)):
    
        if num_list[z] == z+1:
            continue

        is_pandigital = False
        break

    if is_pandigital and i > highest_pandigital:
        highest_pandigital = i

print(f"Highest Prime Pandigital: {highest_pandigital}")
