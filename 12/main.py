#!/usr/bin/env python
from sys import stdin

heightmap = []
map_copy = []
starting_r, starting_c, end_r, end_c = 0,0,0,0

idx = 0
for line in stdin:
    line = list(line.strip('\n'))
    heightmap.append(line)
    if 'S' in line:
        starting_r = idx
        starting_c = line.index('S')
    elif 'E' in line:
        end_r = idx
        end_c = line.index('E')

    idx += 1
map_copy = list(heightmap)

def guard_access(visited, r, c, current_steps):
    # returns true if we can access
    if (r,c) not in visited:
        return True
    return visited[(r,c)] > current_steps + 1
def in_range(elev_map, r, c):
    if r < 0 or c < 0:
        return False
    if r >= len(elev_map):
        return False
    if c >= len(elev_map[0]):
        return False
    return True

def guard_e(i):
    if i == 'E':
        return 'z'
    return i

def bfs(start_r, start_c, end_r, end_c):
    visited = {
            (start_r, start_c) : 0
    }
    #queue = [(start_r, start_c, 'S')]
    queue = []


    for i in range(0, len(heightmap)):
        visited[(i, 0)] = 0
        queue.append((i,0, heightmap[i][0]))



    best_steps = 1000
    while not len(queue) == 0:
        curr_r, curr_c, curr_elevation = queue.pop(0)
        map_copy[curr_r][curr_c] = '.'#map_copy[curr_r][curr_c].
        steps_so_far = visited[(curr_r, curr_c)];
        #print(f'visiting {curr_r},{curr_c} with elev {curr_elevation} and steps {steps_so_far}')

        if (curr_elevation == 'E'):
            best_steps = min(best_steps, steps_so_far)
            continue

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        for i in range(0, 4):
            r = dr[i]
            c = dc[i]

            if in_range(heightmap, curr_r + r, curr_c + c) and guard_access(visited, curr_r+r, curr_c+c, steps_so_far):
                if curr_elevation == 'S' or ord(guard_e(heightmap[curr_r + r][curr_c + c])) - ord(curr_elevation)<= 1:
                    #print(f'\tcurrent_elev: {curr_elevation}, future: {heightmap[curr_r + r][curr_c + c]}')
                    visited[(curr_r + r, curr_c + c)] = steps_so_far + 1
                    queue.append((curr_r + r, curr_c + c, heightmap[curr_r + r][curr_c + c]))
                else:
                    pass
                    #print(f'\t rejected because {curr_elevation} {heightmap[curr_r + r][curr_c + c]}')
            else:
                pass
                #print(f'\trejecting..range={in_range(heightmap, curr_r + r, curr_c + c)}={(curr_r + r, curr_c + c)}')
    #for i in visited:
    #    print(f'visited: {i}')
    return best_steps
print(starting_r, starting_c, end_r, end_c)
print(bfs(starting_r, starting_c, end_r, end_c))
print('done')
for i in map_copy:
    print(''.join(i))
