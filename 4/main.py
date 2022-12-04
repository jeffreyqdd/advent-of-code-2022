#!/usr/bin/env python
from sys import stdin
count = 0;
for line in stdin:
    range1, range2 = line.strip().split(',')
    a,b = map(int, range1.split('-'))
    x,y = map(int, range2.split('-'))
    count += max(0, min(b,y) - max(a,x) + 1) > 0
print(count)
