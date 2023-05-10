#!/usr/bin/python3
for i in range(26):
    ascii = ord('z') if i % 2 == 0 else ord('Z')
    print("{:c}".format(ascii - i), end='')
