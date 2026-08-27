pentagonal_numbers = []

def pentagonal_formula(n):
    Pn = int(n*((3*n)-1)/2)
    return Pn


for i in range(1, 5000):
    pentagonal_numbers.append(pentagonal_formula(i))

print(pentagonal_numbers)

found = False

for j in range(0,len(pentagonal_numbers)):
    if found:
        break

    if j == len(pentagonal_numbers)-1:
        continue

    current = pentagonal_numbers[j]

    for z in range(1, len(pentagonal_numbers)-j):
        if found:
            break

        next = pentagonal_numbers[j+z]

        difference = next - current
        other_difference = abs(current - difference)

        if difference == current:
            continue

        if not difference in set(pentagonal_numbers):
            continue

        print(next, current, difference, other_difference)

        if other_difference in set(pentagonal_numbers):
            print("Found", other_difference)
            found = True
            