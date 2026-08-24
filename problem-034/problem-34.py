import math

total_sum = 0

for i in range(3, 1000000):

    factorial_sum = 0
    for digit in str(i):

        digit = int(digit)

        factorial_sum += math.factorial(digit)

    if factorial_sum == i:
        total_sum+=i

print(total_sum)