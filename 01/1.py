#!/usr/bin/env python3


def run(steps):
    floor = 0
    for step in steps:
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
        else:
            raise Exception('wrong operation', step)
    return floor


with open('input.txt') as lines:
    for line in lines:
        print(run(line.strip()))
