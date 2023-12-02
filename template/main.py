#!/usr/bin/env python
from sys import stdin

for line in stdin:
    # strip newline and skip if line is empty (usually for newline char at EOF)
    line = line.strip()
    if len(line) == 0:
        continue

    print(line)
