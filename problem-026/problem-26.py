import decimal

highest_pattern = 0
highest_number = 0
max_range = 1000
float_nums = []


decimal.getcontext().prec = max_range * 2


def find_patterns(decimal_number, number):
    global highest_number
    global highest_pattern

    for decimal_index in range(0, len(decimal_number)):

        patterns = []

        for pattern_size in range(1, len(decimal_number)//2):

            patterns = [decimal_number[i:i + pattern_size] for i in range(0, len(decimal_number), pattern_size)]
            patterns = patterns[:-1]

            original_number = patterns[0]
            contains_patterns = True

            for items in patterns:

                if original_number != items:
                    contains_patterns = False

            if contains_patterns == True:

                if len(patterns[0]) > highest_pattern:
                    highest_pattern = len(patterns[0])
                    highest_number =  [number, patterns[0]]                

                return 

        decimal_number = decimal_number[1:]


for number in range(2,max_range+1):

    decimal_number = str(decimal.Decimal(1)/decimal.Decimal(number)).split('.')[1]

    find_patterns(decimal_number, number)

print(f"Biggest Pattern Length: {highest_pattern}")
print(f"Number: {highest_number[0]}, Pattern: {highest_number[1]}")