#!/usr/bin/env python3


def run(lines):
    def encode(line):
        res = ['"']
        for c in line:
            if c in ['\\', '"']:
                res.append('\\')
            res.append(c)
        res.append('"')
        # could just return len(res) but useful for debugging
        return ''.join(res)
    total_code = 0
    total_encoded = 0
    for line in lines:
        total_code += len(line)
        encoded = encode(line)
        print(line, encoded)
        total_encoded += len(encoded)
    return total_encoded - total_code


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
