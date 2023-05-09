#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha != ord('q') and alpha != ord('e'):
        print("{:c}".format(alpha), end='')
