#!/usr/bin/env python
from sys import stdin

def on_edge(r,c, grid):
    return r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1

# read
grid = []
for line in stdin:
    row = line.strip('\n')
    grid.append(list(row))

#visible = 0
best = 0
for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        #if on_edge(r, c, grid):
        #    # on edge
        #    visible +=  1
        #    continue
        #else:
        delta_x = [1, -1, 0, 0]
        delta_y = [0, 0, 1, -1]
        max_scenic = 1
        for i in range(0,4):
            dx = delta_x[i]
            dy = delta_y[i]
            tmp_r = r
            tmp_c = c
            scenic_score = 0
            while not on_edge(tmp_r, tmp_c, grid):
                scenic_score += 1
                if grid[r][c] <= grid[tmp_r + dx][tmp_c + dy]:
                    flag = True
                    break
                tmp_r += dx
                tmp_c += dy
            max_scenic *= scenic_score
        best = max(best, max_scenic)
            #if not flag:
            #    visible += 1
            #    break
print(best)
