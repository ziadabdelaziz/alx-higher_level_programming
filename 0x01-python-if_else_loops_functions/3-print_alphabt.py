#!/usr/bin/bash
for alpha in range(97, 123):
    if alpha is not int('q') and alpha is not int('e'):
        print("{:c}".format(alpha), end='')
