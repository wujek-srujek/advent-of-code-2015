#!/usr/bin/env python3


def run(line, iterations):
    def look_and_say(line):
        res = []
        length = len(line)
        i = 0
        while i < length:
            c = line[i]
            count = 0
            while i < length and line[i] == c:
                count += 1
                i += 1
            res.extend((str(count), c))
        return ''.join(res)

    for i in range(iterations):
        line = look_and_say(line)
    return len(line)


with open('input.txt') as lines:
    for line in lines:
        print(run(line.strip(), 50))
