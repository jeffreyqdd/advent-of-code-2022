#!/usr/bin/env python
from sys import stdin
def reverse(n, lst):
        if n <= 0:
            return []
        return lst[:n][::-1] + lst[n:]

crates = {}
total = 0
for line in stdin:
    # we need to figure out if current lin is crate
    #   or if current lin is numbers or move
    if '[' in line:
        x = line.replace(' ', '.').strip('\n')
        x =[x[i:i+4] for i in range(0, len(x), 4)]
        for idx, item in enumerate(x):
            item = item.replace(' ','')
            item = item.replace('[','')
            item = item.replace(']','')
            item = item.replace(',','')
            item = item.replace('.','')
            total = max(total, idx)
            if item != '':
                if idx in crates:
                   crates[idx].append(item)
                else:
                   crates[idx] = [item]
    elif 'move' in line:
         x = line.split(' ')
         cnt = int(x[1])
         src = int(x[3]) - 1
         dest =int(x[5]) - 1
         number_pushed = 0
         for i in range(0,cnt):
            if len(crates[src]) > 0:
                item = crates[src].pop(0)
                crates[dest].insert(0, item)
                number_pushed += 1
         crates[dest] = reverse(number_pushed, crates[dest])
    else:
         print(crates)
ret = ''
for i in range(0, total+1):
    ret += crates[i][0]
print(ret)
