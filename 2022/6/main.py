#!/usr/bin/env python
from sys import stdin

def check(x):
    for i in range(0,len(x)):
        for j in range(0, len(x)):
            if i == j:
                continue
            if x[i] == x[j]:
                return False
    return True

for line in stdin:
    x = line.strip('\n')
    for idx in range(0, len(x)-13):
        data = x[idx:idx+14]
        print(data)
        if check(data):
            print(idx + 14)
            break
