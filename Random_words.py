import random
import sys

filename = 'arknights.txt'
wordlist = []
f = open(filename, 'r', encoding='utf-8')
for line in f:
    if line[0] != '#':
        wordlist.append(line.strip('\n'))
result = random.sample(wordlist, 25)

cnt = 0
for i in range(25):
    if i % 5 == 4:
        print(result[i])
    else:
        print(result[i], end=" ")
