numbers = [0, 1, 2, 3, 4, 5, 6, 7,8,9]
global_var = 1

def print_list(n):
    full_string = ""

    for i in n:
        full_string+=str(i)

    return full_string

def recursive(p, pass_list):
    global global_var

    eight = numbers.index(p)

    check_list = []
    for k in range(eight, 10):
        check_list.append(numbers[k])

    if check_list == pass_list:
        return

    check = True
    for x in range(eight, 10):
            if not x==9:
                if not numbers[x] > numbers[x+1]:
                    check = False

    if check == True:

        value = numbers[eight - 1]
        list = []

        for j in range(eight, 10):
            list.append(numbers[j])
        list.sort()

        for j in list:
            if j > value:
                numbers[eight - 1] = j
                list.remove(j)
                list.append(value)
                break

        list.sort()

        for j in range(0,len(list)):
            numbers[eight+j] = list[j]

        global_var+=1

        print(f"{print_list(numbers)} - {global_var}")
        recursive(p, pass_list)

    if check == False:
        temp_list = []

        for i in range(eight+1, 10):
            temp_list.append(numbers[i])

        temp_list.sort(reverse=True)
    
        recursive(temp_list[0], temp_list)

def calc_lexicographic(times):
    global global_var
    for i in range(1,times):
        nine = numbers.index(9)

        check = True
        for x in range(nine, 10):
                if not x==9:
                    if not numbers[x] > numbers[x+1]:
                        check = False

        if check == True:

            value = numbers[nine - 1]
            list = []

            for j in range(nine, 10):
                list.append(numbers[j])
            list.sort()

            for j in list:
                if j > value:
                    numbers[nine - 1] = j
                    list.remove(j)
                    list.append(value)
                    break

            list.sort()


            for j in range(0,len(list)):
                numbers[nine+j] = list[j]

            global_var+=1
            print(f"{print_list(numbers)} - {global_var}")

        if check == False:
            pass_list = []

            for i in range(nine+1, 10):
                pass_list.append(numbers[i])

            pass_list.sort(reverse=True)
        
            recursive(pass_list[0], pass_list)

calc_lexicographic(481000)
