numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nth_permutation = 1
limit = 100000

def print_list(numbers):
    full_string = ""

    for number in numbers:
        full_string+=str(number)

    return full_string

def find_permutations(current_digit, descending_order):
    global nth_permutation
    global limit

    if nth_permutation == limit:
        return

    current_index = numbers.index(current_digit)
    current_order = []

    for k in range(current_index, 10):
        current_order.append(numbers[k])

    if current_order == descending_order:
        return

    descending = True

    for x in range(current_index, 10):
        if not x==9 and not numbers[x] > numbers[x+1]:
            descending = False

    if descending == True:

        next_digit = numbers[current_index - 1]
        less_than_index_nums = []

        for j in range(current_index, 10):
            less_than_index_nums.append(numbers[j])
        less_than_index_nums.sort()

        for j in less_than_index_nums:
            if j > next_digit:
                numbers[current_index - 1] = j
                less_than_index_nums.remove(j)
                less_than_index_nums.append(next_digit)
                break

        less_than_index_nums.sort()

        for j in range(0,len(less_than_index_nums)):
            numbers[current_index+j] = less_than_index_nums[j]

        nth_permutation+=1

        print(f"{print_list(numbers)} - {nth_permutation}")
        return

    if descending == False:
        ideal_order = []

        for i in range(current_index+1, 10):
            ideal_order.append(numbers[i])

        ideal_order.sort(reverse=True)
    
        find_permutations(ideal_order[0], ideal_order)
        return

while nth_permutation<limit:
    find_permutations(9, [])