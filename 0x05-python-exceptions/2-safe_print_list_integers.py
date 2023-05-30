#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(x):
        elm = my_list[i]
        try:
            print("{:d}".format(elm), end='')
            cnt += 1
        except Exception as e:
            continue

    print()
    return cnt
