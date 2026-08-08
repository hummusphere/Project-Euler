import os

def get_data(path):
    cwd = os.getcwd()
    path = f"{cwd}/{path}"
    data = open(path, "r")
    data=data.read()
    return data

def convert_data_to_list(data):
    return data.replace('"', '').split(',')

def final_score(names):
    sum=0
    i=0
    for x in names:
        i+=1
        local_total=0

        for b in x:
            local_total+=(ord(b)-64)

        local_total*=i
        sum+=local_total

    return sum

data = get_data("problem-022/0022_names.txt")

names = convert_data_to_list(data)
names.sort()

final_score = final_score(names)

print(final_score)