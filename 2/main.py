#!/usr/bin/env python
from sys import stdin

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14

ans = 0
game_id = 1
for line in stdin:
    line = line.strip()
    if len(line) <= 0:
        continue

    game = line.split(':')[1].split(';')
    print(game)
    big_flag = False
    max_red = 0
    max_blue = 0
    max_green = 0
    for draw in game:
        colors = list(map(str.strip, draw.split(',')))
        flag = False
        for color in colors:
            ind = color.split(' ')
            count, col = int(ind[0]), ind[1]
            if col == 'red':
                max_red = max(max_red, count)
            elif col == 'green':
                max_green = max(max_green, count)
            elif col == 'blue':
                max_blue = max(max_blue, count)
    ans += max_red * max_blue * max_green 
        #     if col == 'red' and count > NUM_RED: flag = True
        #        break 
        #     if col == 'blue' and count > NUM_BLUE:
        #        flag = True
        #        break 
        #     if col == 'green' and count > NUM_GREEN:
        #        flag = True
        #        break 
            
        # if flag:
        #     big_flag = True
        #     break
    
    # if not big_flag:
    #     ans += game_id
    game_id += 1
print(ans)