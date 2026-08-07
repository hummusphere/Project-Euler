import math

n = 100

factorial = math.factorial(n)

def find_sum(factorial):
    sum = 0

    for i in str(factorial):
        sum+=int(i)

    return sum

print(find_sum(factorial))