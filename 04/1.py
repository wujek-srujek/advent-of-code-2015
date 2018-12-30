#!/usr/bin/env python3

from hashlib import md5


def run(key):
    i = 0
    while True:
        input = (key + str(i)).encode('ascii')
        if md5(input).hexdigest().startswith('00000'):
            return i
        i += 1


with open('input.txt') as lines:
    for line in lines:
        print(run(line.strip()))
