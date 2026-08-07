amicable_numbers = []

def sum_proper_divisors(current):
    sum = 0
    for x in range(1,current-1):
        if current%x==0:
            sum+=x
    return sum

for i in range(1,10000):
    sum = sum_proper_divisors(i)
    amicable_check = sum_proper_divisors(sum)

    if i==amicable_check and sum!=amicable_check:
        amicable_numbers.append(i)
        print(f"Sum of proper divsors of {i} is {sum}")

sum = 0
for item in amicable_numbers:
    sum+=item

print(amicable_numbers)
print(sum)
