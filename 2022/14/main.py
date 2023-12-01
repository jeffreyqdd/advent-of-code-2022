#!/usr/bin/env python
from sys import stdin

cave_map = [['.' for _ in range(0, 10000)] for _ in range(0,200)]

def render(start_r, end_r, start_c, end_c):
    cave_copy = cave_map.copy()
    cave_copy = cave_copy[start_r:end_r]
    for i in cave_copy:
        print(''.join(i[start_c:end_c]))

def simulate_sand(sand_r=-1, sand_c=499, yeet = 2):
    r = sand_r
    c = sand_c

    if cave_map[r][c] == 'o':
        return True

    while True:
        changed = False
        if cave_map[r+1][c] == '.':
            r += 1
            changed = True
        elif cave_map[r+1][c-1] == '.':
            c -= 1
            r += 1
            changed = True
        elif cave_map[r+1][c+1] == '.':
            c += 1
            r += 1
            changed = True
        else:
            cave_map[r][c] = "o"
            break
        if changed and r >= yeet:
            cave_map[r][c] = "o"
            break
    return False

highest_y = 0
for line in stdin:
    line_points = line.strip('\n').split('->')
    for section in range(0, len(line_points) - 1):
        start = tuple(map(int, line_points[section].split(',')))
        end = tuple(map(int,line_points[section + 1].split(',')))
        highest_y = max(highest_y, max(start[1], end[1]))
        if start[0] == end[0]:
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                cave_map[i-1][start[0]-1] = '#'
        else:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                cave_map[start[1]-1][i-1] = '#'

print('high3st y', highest_y)
cnt = 1
while not simulate_sand(yeet = highest_y + 0):
    cnt += 1
    render(0, 11, 485, 517)
    print()
print(cnt-1)


