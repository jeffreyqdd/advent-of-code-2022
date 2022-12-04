#!/usr/bin/env python

from sys import stdin
count = 0;
for line in stdin:
    range1, range2 = line.strip().split(',')
    a,b = range1.split('-')
    x,y = range2.split('-')
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)

    if max(0, min(b,y) - max(a,x) + 1) > 0:
        count += 1

print(count)
