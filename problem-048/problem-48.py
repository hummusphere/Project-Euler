sum = 0

for i in range(1,1001):
    sum+= i**i

sum = int(str(sum)[-10:])
print(sum)