#!/usr/bin/bash python3


def permutations_no_repetitions(lst, *, r=None):
    if r == None:
        r = len(lst)
    if r > len(lst):
        raise ValueError('r > len(lst)')
    if r < 0:
        raise ValueError('r < 0')

    def perms(l, depth):
        if not l or depth == r:
            yield ()
        else:
            # each iteration uses the current element + recursively
            # permutations of the list minus the current element
            for i, e in enumerate(l):
                for perm in perms(l[:i] + l[i+1:], depth+1):
                    yield (e,) + perm
    return perms(lst, 0)


def permutations_with_repetitions(lst, *, r=None):
    if r == None:
        r = len(lst)
    if r < 0:
        raise ValueError('r < 0')

    def perms(l, depth):
        if not l or depth == r:
            yield ()
        else:
            # each iteration uses the current element + recursively
            # permutations of the same list (elements can repeat)
            for i, e in enumerate(l):
                for perm in perms(l, depth+1):
                    yield (e,) + perm
    return perms(lst, 0)


def combinations_no_repetitions(lst, *, r=None):
    if r == None:
        r = len(lst)
    if r > len(lst):
        raise ValueError('r > len(lst)')
    if r < 0:
        raise ValueError('r < 0')

    def combs(l, depth):
        if not l or depth == r:
            yield ()
        else:
            # each iteration uses the current element + recursively
            # combinations of the list starting with the next element
            # stopping iteration early will make sure later elements
            # will not occur twice (they will occur once by recursion
            # starting at a point after the current element)
            for i in range(len(l) - (r - depth - 1)):
                for perm in combs(l[i+1:], depth+1):
                    yield (l[i],) + perm
    return combs(lst, 0)


def combinations_with_repetitions(lst, *, r=None):
    if r == None:
        r = len(lst)
    if r < 0:
        raise ValueError('r < 0')

    def combs(l, depth):
        if not l or depth == r:
            yield ()
        else:
            # each iteration uses the current element + recursively
            # combinations of the list starting with the current element
            for i, e in enumerate(l):
                for perm in combs(l[i:], depth+1):
                    yield (e,) + perm
    return combs(lst, 0)


# tests


def f(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def check(tested_fn, count_fn, *, n=5, r=None, debug=False):
    elements = [i for i in range(1, n + 1)]
    r_range = range(0, n + 1) if r == None else range(r, r + 1)
    for r in r_range:
        expected_count = count_fn(n, r)
        got = []
        for p in tested_fn(elements, r=r):
            got.append(p)
        failed = len(got) != expected_count
        if failed:
            print('!!! failed')
        if failed or debug:
            print('{} for elements={}, n={}, r={}, expected {}, got {}'.format(
                tested_fn.__name__, elements, n, r, expected_count, len(got)))
            for p in got:
                print(p)


check(permutations_no_repetitions, lambda n, r: f(n)//f(n-r))

check(permutations_with_repetitions, lambda n, r: n**r)

check(combinations_no_repetitions, lambda n, r: f(n)//(f(r)*f(n-r)))

check(combinations_with_repetitions, lambda n, r: f(r+n-1)//(f(r)*f(n-1)))
