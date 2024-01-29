#!/usr/bin/python3
"""this dox contains func UTF-8 Validation"""


def validUTF8(data):
    """func to determent if given data represent valid"""
    num = 0
    task_1 = 1 << 7
    task_2 = 1 << 6

    for x in data:
        task_b = 1 << 7

        if num == 0:
            while task_b & x:
                num += 1
                task_b = task_b >> 1

            if num == 0:
                continue
            if num == 1 or num > 4:
                return False

        else:
            if not (x & task_1 and not (x & task_2)):
                return False

        num -= 1

    if num == 0:
        return True

    return False
