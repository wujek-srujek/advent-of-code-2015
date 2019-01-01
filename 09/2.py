#!/usr/bin/env python3

import re


def run(lines):
    p = re.compile(r'(.+) to (.+) = (\d+)')
    path2dist = dict()
    all_cities = set()
    for line in lines:
        start, end, dist = p.findall(line)[0]
        dist = int(dist)
        path2dist[start, end] = dist
        path2dist[end, start] = dist
        all_cities.add(start)
        all_cities.add(end)

    def all_paths(cities, depth):
        # calculates all permutations without repetitions
        # i.e. paths from start city to end city visiting
        # each city only once
        if not cities:
            yield ()
        else:
            # each iteration uses the current element + recursively
            # permutations of the list minus the current element
            for i, c in enumerate(cities):
                for path in all_paths(cities[:i] + cities[i+1:], depth+1):
                    yield (c,) + path

    def distance(path):
        # calculates the distance for the path
        dist = 0
        for start, end in zip(path, path[1:]):
            dist += path2dist[start, end]
        return dist

    # calculate distance (if possible) for each path and store the minimum
    max_dist = None
    max_path = None
    for path in all_paths(list(all_cities), 0):
        dist = distance(path)
        if not max_dist or dist > max_dist:
            max_dist = dist
            max_path = path
    return max_path, max_dist


with open('input.txt') as lines:
    print(run((line.strip() for line in lines)))
