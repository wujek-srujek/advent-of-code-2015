#!/usr/bin/env python3


def run(lines):
    def decode(line):
        # assumes the string is correctly formatted
        line = line[1:-1]
        res = []
        i = 0
        while i < len(line):
            c = line[i]
            if c == '\\':
                c = line[i + 1]
                i += 2
                if c == 'x':
                    code = line[i:i + 2]
                    c = chr(int(code, 16))
                    i += 2
            else:
                i += 1
            res.append(c)
        # could just return len(res) but useful for debugging
        return ''.join(res)
    total_code = 0
    total_decoded = 0
    for line in lines:
        total_code += len(line)
        # actually, a simple eval would work, but it is evil
        # decoded = eval(line)
        decoded = decode(line)
        total_decoded += len(decoded)
    return total_code - total_decoded


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
