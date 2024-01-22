#!/usr/bin/python3
import sys


def func_print(d_sc, total):
    """func to print
    args:
        d_sc: dictionary of status code
        total: total of file
    return:
        nothing
    """
    print("File size: {}".format(total))

    for k, v in sorted(d_sc.items()):
        if v != 0:
            print("{}: {}".format(k, v))


total = 0
cd = 0
count = 0

d_sc = {"200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0}

try:
    for li in sys.stdin:
        p_line = li.split()
        p_line = p_line[::-1]

        if len(p_line) > 2:
            count += 1

            if count <= 10:
                total += int(p_line[0])
                cd = p_line[1]

                if (cd in d_sc.keys()):
                    d_sc[cd] += 1

            if (count == 10):
                func_print(d_sc, total)
                count = 0
finally:
    func_print(d_sc, total)
