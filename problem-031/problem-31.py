currency = [200, 100, 50, 20, 10, 5, 2, 1]
ways = 1

def add_numbers_in_list(numbers_list):

    sum = 0

    for number in numbers_list:

        sum+=number

    return sum


def find_solutions_for(original_number, number, numbers_list):
    global ways

    og_list = numbers_list.copy()
    index_of_number = currency.index(number)
    next_subdivision = currency[index_of_number+1]
    divisions = (original_number-add_numbers_in_list(numbers_list))//next_subdivision

    if not next_subdivision == 1: 
        for i in range(divisions, -1, -1):

            for k in range(0, i):
                numbers_list.append(next_subdivision)

            if add_numbers_in_list(numbers_list) == original_number: 
                ways+=1
                print(f"Number: {numbers_list}, {ways}")

            if add_numbers_in_list(numbers_list) != original_number and next_subdivision != 1:
                find_solutions_for(original_number, next_subdivision, numbers_list)

            numbers_list = og_list.copy()

        return numbers_list

    for k in range(0, divisions):
        numbers_list.append(next_subdivision)

    ways+=1
    print(f"Number: {numbers_list}, {ways}")

    numbers_list = og_list.copy()
    return numbers_list

find_solutions_for(200, 200, [])
print(ways)