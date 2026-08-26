targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
results = []

current = 1
index = 1


while not len(targets) == 0:
    print(current)

    for i in range(0, len(str(current))):

        if index in targets:
            results.append(int(str(current)[i]))
            targets.remove(index)

        index+=1
    
    current+=1

product = 1

for k in results:
    product*=k

print(results)
print(product)