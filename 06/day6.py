import numpy as np
from functools import reduce

data = []
'''      
with open("day6.txt") as f:
    for line in f:
        new = line.split(' ')
        
        data.append([x.strip() for x in new if x.strip() != ''])

data = np.array(data).T

day1 = 0
for i in data:
    if i[-1] == "*":
        day1 += reduce(lambda x, y: x * y, map(int, i[:-1]))
    else:
        day1 += sum(map(int, i[:-1]))
'''

with open("day6.txt") as f:
    for line in f:
        data.append(line.replace("\n", ""))

data = np.array([[i for i in j] for j in data])

day2 = 0
subtotal = 0
operator = ''
for i in data.T:
    if all(digit ==' ' for digit in i):
        day2 += subtotal
        subtotal = 0
        continue

    if i[-1] != ' ':
        operator = i[-1]

    num = int("".join(digit for digit in i[:-1] if digit != ' '))

    if operator =="+":
        subtotal += num
    else:
        subtotal = max(subtotal, 1)*num

day2 += subtotal # Range doesnt add last subtotal

print(day2)