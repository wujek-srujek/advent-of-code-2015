#!/usr/bin/env python3

import re


def run(lines):
    def needed(l, w, h):
        x = min(l+w, w+h, h+l)
        return 2*x + l*w*h
    p = re.compile(r'(\d+)x(\d+)x(\d+)')
    total = 0
    for line in lines:
        l, w, h = map(int, p.findall(line)[0])
        total += needed(l, w, h)
    return total


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
