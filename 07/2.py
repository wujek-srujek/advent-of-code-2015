#!/usr/bin/env python3

import re


def run(lines):
    ops = {
        'AND': lambda a, b: a & b,
        'OR': lambda a, b: a | b,
        'NOT': lambda a: ~a,
        'LSHIFT': lambda a, b: a << b,
        'RSHIFT': lambda a, b: a >> b,
        '': lambda a: a
    }
    line_p = re.compile('(.+) -> ([a-z]+)')
    source_p = re.compile('(?:(.+) )?([A-Z]+) (.+)')
    number_p = re.compile('\d+')
    identifier_p = re.compile('[a-z]+')

    def parse_line(line):
        # returns (wire name, value)
        # value is:
        # (True, value) if resolved to a value
        # (False, (expression)) if unresolved
        # expression is:
        # (operator function, [args])
        # each arg is:
        # (True, value) if resolved to a value
        # (False, key) if unresolved
        source, wire = line_p.findall(line)[0]
        if number_p.fullmatch(source):
            # a hardcoded value
            return wire, (True, int(source))
        if identifier_p.fullmatch(source):
            # a value of another wire
            return wire, (False, (ops[''], [(False, source)]))
        arg1, op, arg2 = source_p.findall(source)[0]
        args = []

        def append_arg(arg):
            args.append((True, int(arg)) if number_p.fullmatch(
                arg) else (False, arg))
        # arg1 is unset for NOT
        if arg1:
            append_arg(arg1)
        append_arg(arg2)
        return wire, (False, (ops[op], args))
    wire2value = dict()
    for line in lines:
        wire, value = parse_line(line)
        wire2value[wire] = value
    # override according to instructions
    wire2value['b'] = True, 46065

    def get(wire):
        # gets the value, resolving operation arguments if necessary
        # each resolved argument gets saved in the dictionary replacing
        # the original parsed expression
        resolved, value = wire2value[wire]
        if not resolved:
            op, args = value
            resolved_args = []
            for resolved, valueOrKey in args:
                if resolved:
                    resolved_args.append(valueOrKey)
                else:
                    val = get(valueOrKey)
                    resolved_args.append(val)
            # convert signed to unsigned
            value = op(*resolved_args) & 0xFFFF
            # replace the value in the dict
            wire2value[wire] = True, value
        return value
    return get('a')


with open('input.txt') as lines:
    print(run(lines))
