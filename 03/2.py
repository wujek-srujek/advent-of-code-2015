#!/usr/bin/env python3

from collections import defaultdict


def run(directions):
    # grid saves how many times the house was already visited
    grid = defaultdict(int)

    def deliver(directions):
        # initial location
        x, y = 0, 0
        # initial house
        grid[x, y] += 1
        for direction in directions:
            # directions move around the grid
            if direction == '^':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == 'v':
                y += 1
            elif direction == '<':
                x -= 1
            else:
                raise Exception('invalid direction', direction)
            grid[x, y] += 1
    # traverse every other direction
    # even for santa
    deliver(directions[i] for i in range(0, len(directions), 2))
    # uneven for robo-santa
    deliver(directions[i] for i in range(1, len(directions), 2))
    return len(grid)


with open('input.txt') as lines:
    for line in lines:
        print(run(line.strip()))
