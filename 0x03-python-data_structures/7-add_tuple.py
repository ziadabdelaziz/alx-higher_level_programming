#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = 1
    a, b = tuple_a, tuple_b
    for tup in [tuple_a, tuple_b]:
        if isinstance(tup, int):
            tup = (tup, 0)
        elif len(tup) == 0:
            tup = (0, 0)
        elif len(tup) == 1:
            tup = (tup[0], 0)
        else:
            tup = (tup[0], tup[1])

        if first:
            a = tup
            first = 0
        else:
            b = tup

    return (a[0] + b[0], a[1] + b[1])
