F1 = 1
F2 = 1
index = 2

def add_sequence(first, second):
    return first + second

while len(str(F2)) < 1000:
    index+=1
    F1, F2 = F2, add_sequence(F1, F2)

print(index)