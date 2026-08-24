import math

max_value = 1000001
found_numbers = [2, 3, 5]

def check_prime(num):

    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num%i == 0:
            return False

    return True


for i in range(6, max_value):

    if i%2 == 0 or i%3 == 0 or i%5 == 0:
        continue

    print(i)
    digit_list = []
    shifted = []

    for digit in str(i):
        shifted.append(' ')
        digit_list.append(int(digit))

    list_len = len(digit_list)

    full_check = True

    for j in range(0, list_len):
        shifted = []
        for digit in str(i):
            shifted.append(' ')
    
        for digit in range(0,list_len):
            current_index = digit
            current_index-=1

            if not current_index == -1:
                shifted[current_index] = digit_list[digit]

            else:
                shifted[list_len-1] = digit_list[digit]

        digit_list = shifted.copy()

        str_number = ''

        for k in shifted:
            str_number+=str(k)

        int_number=int(str_number)

        if check_prime(int_number) == False:
            full_check = False

    if full_check == True:
        found_numbers.append(i)

total_sum = 0
for c in found_numbers:
    total_sum+=1

print(found_numbers)
print(total_sum)
