max_value = 1000000
sum = 0

def fifth_power_digits(num):
    global sum

    str_num = str(num)
    total = 0

    for digit in str_num:
        total+=(int(digit)**5)

    if total == num:
        sum+=num

    return

for i in range(2, max_value+1):
    fifth_power_digits(i)

print(f"sum: {sum}")