#!/usr/bin/env python
from sys import stdin

row_coords = [0,0,0,0,0,0,0,0,0,0]
col_coords = [0,0,0,0,0,0,0,0,0,0]
unique_tail_loc = {(0,0)}

def debug_board(max_r = 40, max_c = 40):
    half_r = int(max_r / 2)
    half_c = int(max_c / 2)

    board = [['.' for i in range(0, max_c)] for j in range(0, max_r)]
    for i in range(0,10):
        i = 9 - i
        if i == 0:
            board[row_coords[i] + half_r][col_coords[i] + half_c] = 'H'
        else:
            board[row_coords[i] + half_r][col_coords[i] + half_c] = str(i)

    board[half_r][half_c]='s'
    for i in board:
        print(''.join(i))

def direction_decode(dir):
    # row_delta, col_delta
    if dir == 'R':
        return 0, 1
    elif dir == 'U':
        return -1, 0
    elif dir == 'L':
        return 0, -1
    else:
        return 1, 0

def follow(head_r, head_c, tail_r, tail_c, dr, dc, diag=False):
    man_dist = abs(head_r - tail_r) + abs(head_c - tail_c)
    if man_dist <= 1:
        return 0, 0, False
    elif man_dist <= 2 and head_r != tail_r and head_c != tail_c:
        return 0, 0, False
    # check if directly
    if head_r == tail_r or head_c == tail_c:
        print('yeet')
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        for i in range(0,4):
            dist = abs(head_r-(tail_r + dr[i])) + abs(head_c-(tail_c + dc[i]))
            if dist <= 1:
                return dr[i], dc[i], False
        assert -1 == 0
        return dr, dc, False
    elif diag:
        return dr, dc, True
    else:
        # need to move diagonally
        return None, None, True

for line in stdin:
    line = line.strip('\n').split(' ')
    direction, distance = str(line[0]), int(line[1])
    delta_r, delta_c = direction_decode(direction)

    print(f"========{direction}, {distance}")
    for i in range(0, distance):
        prev_r = 0
        prev_c = 0
        print(*[f'{i:3d}' for i in row_coords])
        print(*[f'{i:3d}' for i in col_coords])
        print()
        diag = False
        for tail_count in range(0, 10): # bruh.. we have 9 tails...
            if tail_count == 0:
                # head
                row_coords[tail_count] += delta_r
                col_coords[tail_count] += delta_c
                prev_r = delta_r
                prev_c = delta_c
                print('\t...head')
            else:
                follow_r, follow_c, diag = follow(row_coords[tail_count-1], col_coords[tail_count-1],
                                            row_coords[tail_count], col_coords[tail_count],
                                            prev_r, prev_c, diag)

                if follow_r is None or follow_c is None:
                    print('\t...diag')
                    tmp_r = row_coords[tail_count]
                    tmp_c = col_coords[tail_count]
                    row_coords[tail_count] = row_coords[tail_count - 1] - prev_r
                    col_coords[tail_count] = col_coords[tail_count - 1] - prev_c
                    prev_r = row_coords[tail_count] - tmp_r
                    prev_c = col_coords[tail_count] - tmp_c
                else:
                    if diag:
                        print('\t...diag')
                    else:
                        print('\t...follow')
                    row_coords[tail_count] += follow_r
                    col_coords[tail_count] += follow_c
                    prev_r = follow_r
                    prev_c = follow_c

                if tail_count == 9:
                    unique_tail_loc.add((row_coords[tail_count], col_coords[tail_count]))
        #Edebug_board()
print(len(unique_tail_loc))
