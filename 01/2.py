#!/usr/bin/env python3


def run(steps):
    floor = 0
    i = 1
    for step in steps:
        if step == '(':
            floor += 1
        elif step == ')':
            floor -= 1
        else:
            raise Exception('wrong operation', step)
        if floor == -1:
            break
        i += 1
    return i


with open('input.txt') as lines:
    for line in lines:
        print(run(line.strip()))
