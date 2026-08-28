not_found = True
n = 2

pentagonal_nums = []
hexagonal_nums = []

while not_found:

    triangle_num = n*(n+1)/2
    pentagonal_num = n*(3*n-1)/2
    hexagonal_num = n*(2*n-1)

    print(triangle_num)

    pentagonal_nums.append(pentagonal_num)
    hexagonal_nums.append(hexagonal_num)

    if triangle_num in set(pentagonal_nums) and triangle_num in set(hexagonal_nums) and not triangle_num == 40755:
        not_found = False

    n+=1
