#!/usr/bin/env python
from sys import stdin

data = []
for line in stdin:
    x = line.strip('\n')
    if x == '':
        continue
    data.append(eval(x))


def compare(a, b):
    # return 0 if should proceeed
    # return [1, inf) if wrong order
    # return (-inf,-1] if in correct order
    if isinstance(a, list) and isinstance(b, list):
        for i in range(0, max(len(a), len(b))):
            if len(a) <= i:
                return -1 # left list runs out of stuff first
            if len(b) <= i:
                return 1 # right list runs out of stuff first
            result = compare(a[i], b[i])
            if result != 0:
                return result
    elif isinstance(a, list):
        # b is not list,
        return compare(a, [b])
    elif isinstance(b, list):
        # a is not list
        return compare([a], b)
    else:
        return a - b

    return 0
sum = 0

#for idx in range(0, int(len(data) / 2)):
#    a = data[idx*2]
#    b = data[idx*2 + 1]
#
#    # compare
#    res = compare(a,b)
#    if res < 0:
#        sum += idx + 1
data.append([[2]])
data.append([[6]])
for i in range(0, len(data)):
    for j in range(0, len(data)):
        if i == j:
            continue

        if compare(data[i], data[j]) < 0:
            tmp = data[i]
            data[i] = data[j]
            data[j] = tmp

for i in data:
    print(i)

print((data.index([[2]])+1) * (data.index([[6]])+1))
