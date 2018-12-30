#!/usr/bin/env python3


def run(lines):
    def is_nice(word):
        vowels = 0
        doubles = False
        # iterate overlapping pairs
        for l, r in zip(word, word[1:]):
            # just check the first letter in pair, the other one in next iteration
            if l in 'aeiou':
                vowels += 1
            if l == r:
                doubles = True
            if (l, r) in {('a', 'b'), ('c', 'd'), ('p', 'q'), ('x', 'y')}:
                # naughty no matter what
                return False
        # check last letter for vowel
        if r in 'aeiou':
            vowels += 1
        return vowels >= 3 and doubles
    nice_count = 0
    for line in lines:
        if is_nice(line):
            nice_count += 1
    return nice_count


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
