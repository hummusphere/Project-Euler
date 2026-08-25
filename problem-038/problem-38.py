max = 10000
panditial_list = [1,2,3,4,5,6,7,8,9]

not_found = True

def check_pandigital(number):

    digit_list = []

    for k in str(number):
        digit_list.append(int(k))

    digit_list.sort()

    if digit_list == panditial_list:
        return True

    return False


while not_found:

    concation = ''
    i = 1

    while len(concation) < 9:
        add_concative = i * max
        concation+=str(add_concative)
        i+=1

    if len(concation) == 9:
        if check_pandigital(concation) == True:
            print(concation)
            not_found = False

    max-=1

    if max == 0:
        not_found = False