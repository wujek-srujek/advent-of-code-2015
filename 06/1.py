#!/usr/bin/env python3

from collections import defaultdict
import re


def run(lines):
    grid = defaultdict(bool)
    p = re.compile(r'.+?(\d+),(\d+).+?(\d+),(\d+)')
    for line in lines:
        if 'turn on' in line:
            def op(light): return True
        elif 'turn off' in line:
            def op(light): return False
        else:
            def op(light): return not light
        x1, y1, x2, y2 = map(int, p.findall(line)[0])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x, y] = op(grid[x, y])
    count = 0
    for x, y in grid.keys():
        if grid[x, y]:
            count += 1
    return count


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
