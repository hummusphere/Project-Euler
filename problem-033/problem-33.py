global_denominators = []
global_numerators = []

def dont_meet_criteria(first_number, second_number):
    global global_denominators
    global global_numerators

    letter_one = []
    letter_two = []

    for letter in str(first_number):
        letter_one.append(letter)

    for letter in str(second_number):
        letter_two.append(letter)

    if first_number/second_number >= 1:
        return True
    
    if letter_one[0] == letter_one[1] or letter_two[0] == letter_two[1]:
        return True

    if '0' in letter_one or '0' in letter_two:
        return True
    
    if letter_two[0] in letter_one:
        letter_one.remove(letter_two[0])
        letter_one = int(letter_one[0])

        letter_two.pop(0)
        letter_two = int(letter_two[0])

        if letter_one/letter_two == first_number/second_number:
            global_numerators.append(first_number)
            global_denominators.append(second_number)
            return False

    elif letter_two[1] in letter_one:
        letter_one.remove(letter_two[1])
        letter_one = int(letter_one[0])

        letter_two.pop(1)
        letter_two = int(letter_two[0])

        if letter_one/letter_two == first_number/second_number:
            global_numerators.append(first_number)
            global_denominators.append(second_number)
            return False

    return True


for first_number in range(11, 100):
    for second_number in range(11,100):

        if dont_meet_criteria(first_number, second_number):
            continue

        numerator_product = 1
        for j in global_numerators:
            numerator_product*=j

        denominator_product = 1
        for k in global_denominators:
            denominator_product*=k

solution = 1/(numerator_product/denominator_product)
print(solution)
        
