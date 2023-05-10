#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii = ord(c)
        if 96 < ord(c) < 123:
            ascii = ord(c) - 32
        print('{:c}'.format(ascii), end='')
    print()
