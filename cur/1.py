#!/usr/bin/env python3


def run(line):
    def inc(word):
        # find the first non-z and increase it
        # start looking from last char
        for i, c in enumerate(reversed(word)):
            if c != 'z':
                i = len(word) - i - 1
                break
        return word[0:i] + chr(ord(c) + 1) + word[i+1:]

    return inc(line)


with open('input-ex.txt') as lines:
    for line in lines:
        print(run(line.strip()))
