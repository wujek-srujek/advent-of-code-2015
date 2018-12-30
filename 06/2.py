#!/usr/bin/env python3

from collections import defaultdict
import re


def run(lines):
    grid = defaultdict(int)
    p = re.compile(r'.+?(\d+),(\d+).+?(\d+),(\d+)')
    for line in lines:
        if 'turn on' in line:
            def op(light): return light + 1
        elif 'turn off' in line:
            def op(light): return light - 1 if light > 0 else 0
        else:
            def op(light): return light + 2
        x1, y1, x2, y2 = map(int, p.findall(line)[0])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x, y] = op(grid[x, y])
    total = 0
    for x, y in grid.keys():
        total += grid[x, y]
    return total


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
