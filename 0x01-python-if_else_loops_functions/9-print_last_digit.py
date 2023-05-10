#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        last = ((number * -1) % 10)
    else:
        last = number % 10
    print(last, end='')
    return last
