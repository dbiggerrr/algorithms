def func(var, b):
    key = 0
    for i in range(len(var)):
        if var[i] == b:
            key += 1
    return key


with open('input55.txt', 'r', encoding="Cp1252") as inputfile:
    f = inputfile.readlines()
items = []
for i in f:
    items.append(i)
    
word = items[0]
N = int(items[1])
words = []
for i in range(2, N + 2):
    words.append(items[i])
for w in words:
    for j in range(len(w)):
        if func(w, w[j]) > func(word, w[j]):
            N -= 1
            break

file1 = open("output55.txt", "w")
file1.write(str(N))
file1.close()
