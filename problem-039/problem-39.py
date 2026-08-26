import math

max = 1000
highest = 0
highest_val = 0

for p in range(1, 1000):
    print(p)

    solutions = 0

    for one in range(1, p//3):

        for two in range(one, (p-one)//2):

            three = p - one - two

            if math.sqrt(one**2 + two**2) == three:

                solutions += 1

    if solutions > highest:
        highest = solutions
        highest_val = p


print(f"Highest Value: {highest_val}")