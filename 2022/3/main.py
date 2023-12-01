#!/usr/bin/env python
import fileinput
with fileinput.input('2.in') as f:
    inputs = list(f)
    total = 0
    for i in range(0, int(len(inputs)/3)):
        a = inputs[i*3].strip()
        b = inputs[i*3 + 1].strip()
        c = inputs[i*3 + 2].strip()
        x = ord(list(set(a) & set(b) & set(c))[0])
        total += x - ord('a') + 1 if x - ord('a') >= 0 else (x - ord('A') + 27)
    print(total)

