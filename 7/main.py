#!/usr/bin/env python
import os
from sys import stdin

# key=dir, value = size
seen_files = {}
tree = {}
current_dir = '/'
for line in stdin:
    line = line.strip('\n')
    if line == '':
        continue
    # command
    if 'cd' in line and '$' in line:
        args = line.split(' ')
        cd_dir = args[2]
        print(line)
        if cd_dir != '/':
            if cd_dir != '..':
                current_dir = os.path.join(current_dir, cd_dir)
            else:
                current_dir = os.path.dirname(
                        current_dir)
            print(current_dir)
    elif 'ls' in line and '$' in line:
        continue
    elif 'dir' in line and '$' not in line and '.' not in line:
        continue
    else:
        assert '$' not in line
        print('yeeting==========================')
        args = line.split(' ')
        print(args)
        size = int(args[0])
        copy_of_dir = str(current_dir)
        file = os.path.join(copy_of_dir, args[1])
        print(f'\t\t\trepeat: {file}')
        if file in seen_files:
            continue
        else:
            seen_files[file] = 1

        while True:
            print(copy_of_dir)
            if copy_of_dir in tree:
                tree[copy_of_dir] += size;
            else:
                tree[copy_of_dir] = size;
            if copy_of_dir == '/':
                break
            else:
                copy_of_dir = os.path.dirname(
                    copy_of_dir)
print(tree)

root_size = tree['/']
need = 30000000 - (70000000 - root_size)
best = 10000000000
for k, v in tree.items():
    print(k , ' ', v, end = '')
    if v > need and v < best:
        best = v
        print('...new best',end='')
    print()

print('root size: ', root_size)
print('need:', need)
print('best', best)
#print(sum([v for k, v in tree.items() if v <= 100_000]))
