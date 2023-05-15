#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    length = len(my_string)
    cur, prev = 0, 0

    while cur < length:
        if my_string[cur] in ['c', 'C']:
            new_string += my_string[prev:cur]
            prev = cur + 1
        cur += 1

    if prev < cur:
        new_string += my_string[prev:cur]

    return new_string
