#!/usr/bin/env python3

from collections import defaultdict


def run(lines):
    def is_nice(word):
        around_letter = False
        # could do with regexes and capture group refs
        # (.).\1' and (..).+\1
        # but let's invent something more fun
        # iterate in overlapping triplets
        for _1, _, _3 in zip(word, word[1:], word[2:]):
            if _1 == _3:
                around_letter = True
        i = 0
        pair2index = defaultdict(list)
        pair2count = defaultdict(int)
        # iterate overlapping pairs
        for _1, _2 in zip(word, word[1:]):
            # save each pair and its starting location
            pair2index[_1, _2].append(i)
            # save count for each pair
            pair2count[_1, _2] += 1
            i += 1
        has_pair = False
        # find the first pair that occurs more than once
        # at indices with diff > 1 (no overlap)
        for pair, count in pair2count.items():
            if count > 1:
                indices = pair2index[pair]
                for i1, i2 in zip(indices, indices[1:]):
                    if i2 - i1 > 1:
                        has_pair = True
                        break
                else:
                    continue
                break
        return around_letter and has_pair
    nice_count = 0
    for line in lines:
        if is_nice(line):
            nice_count += 1
    return nice_count


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
