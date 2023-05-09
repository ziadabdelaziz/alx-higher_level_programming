#!/usr/bin/python
for alpha in range(97, 123):
    if alpha != ord('q') and alpha != ord('e'):
        print("{:c}".format(alpha), end='')
