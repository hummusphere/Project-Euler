max = 1000000
sum = 0
numbers_list = []
binary_list = []

def convert_to_binary(input):

    binary_number = ''

    quotient = input

    add_zeros = 0

    while not quotient == 0:
        remainder =  quotient % 2

        if remainder == 0 and not quotient == 0 and input % 2 == 0:
            add_zeros+=1

        quotient = quotient // 2
        binary_number += str(remainder)

    for i in range(0, add_zeros):
        binary_number+='0'
        
    binary_number = int(binary_number)

    return binary_number

def check_palindromic(input):

    palindromic = True

    list_input = []

    for digit in str(input):
        list_input.append(digit)

    for i in range(0, len(list_input)):
        if not list_input[i] == list_input[len(list_input)-(i+1)]:
            palindromic = False

    return palindromic

for i in range(1, max):
    binary_i = convert_to_binary(i)

    if check_palindromic(i) == True and check_palindromic(binary_i) == True:
        sum+=i
        numbers_list.append(i)
        binary_list.append(binary_i)

print(sum)


