minimum = 2
maximum = 100

sequence = []

for i in range(minimum, maximum+1):
    for k in range(minimum, maximum+1):
        if not i**k in sequence:
            sequence.append(i**k)

sequence.sort()
print(len(sequence))