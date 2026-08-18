max_num = 1001

i = 1
j = 2

total = 1

while i < max_num**2:
    for k in range(0,4):
        i+=j
        total+=i
    j+=2

print(total)