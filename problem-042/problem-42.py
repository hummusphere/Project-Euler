import os, string

triangle_words = 0

def get_data(path):

    cwd = os.getcwd()
    path = f"{cwd}/{path}"

    data = open(path, "r")
    data = data.read()

    return data

def sort_data(data):
    return data.replace('"', '').split(',')

def get_word_value(word):
    sum = 0

    for letter in word:
        sum += ord(letter.lower()) - 96


    return sum


data = get_data("problem-042/0042_words.txt")
data = sort_data(data)

for word in data:

    word_value = get_word_value(word)

    triangle_number = 0
    n = 0

    while triangle_number < word_value:
        n+=1
        triangle_number = (1/2)*n*(n+1)

    if triangle_number == word_value:
        triangle_words+=1

print(triangle_words)