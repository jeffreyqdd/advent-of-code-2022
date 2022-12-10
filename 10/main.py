#!/usr/bin/env python
from sys import stdin

def should_draw(sprite, pixel):
    return abs(sprite-pixel) <= 1

cycle_count = 0
register = 1
signal_strength = 0
image = ""

def render():
    global cycle_count, registre, signal_strngth, image
    if cycle_count % 40 == 0 and cycle_count > 0:
        image += '\n'
    if should_draw(register, cycle_count % 40):
        image += "#"
    else:
        image += '.'

for line in stdin:
    instruction = line.strip('\n')
    render()
    if 'noop' == instruction:
        cycle_count += 1
    else:
        x = int(line.split(' ')[1])
        cycle_count += 1
        render()
        cycle_count += 1
        register += x

print(signal_strength)
print(image)
