max_amount = 2000
ideal_list = [1,2,3,4,5,6,7,8,9]
found_list = []
sum = 0

for i in range (1, max_amount):
    for x in range(1, max_amount):

        temp_list = []

        for k in str(i):
            temp_list.append(int(k))

        for j in str(x):
            temp_list.append(int(j))

        for z in str(i*x):
            temp_list.append(int(z))

        temp_list.sort()

        check = temp_list == ideal_list

        if check and not i*x in found_list:
            sum+=i*x
            print(f"{i} * {x} = {i*x}, current sum: {sum}")
            found_list.append(i*x)

print(sum)