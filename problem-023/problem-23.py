abundant_numbers = []
abundant_sums = []

def find_abundant_numbers(scale, store):
    total_sum=0
    for i in range(1, scale):
        total_sum+=i
        print(f"i: {i}")
        sum=0
        for x in range(1, i):
            if i%x==0:
                sum+=x
        if sum>i:
            store.append(i)

    return {"store":store, "sum": total_sum}

def find_abundant_sums(limit, numbers):
    total_sum = 0

    numbers = set(numbers)

    for i in range(limit,0,-1):
        print(i)
        for x in numbers:
            if x >= i:
                break

            if i - x in numbers:
                total_sum += i
                break

    return total_sum

abundant_numbers = find_abundant_numbers(28124, abundant_numbers)
abundant_sums = find_abundant_sums(28123, abundant_numbers["store"])

print(abundant_numbers["sum"]-abundant_sums)