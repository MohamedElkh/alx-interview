#!/usr/bin/python3
"""this func contain a method to calc the fewest num of opera"""


def minOperations(n):
    """func to return the fewest num of opers to res chara in file"""
    ops = 0
    min_opr = 2

    while n > 1:
        while n % min_opr == 0:
            ops += min_opr
            n /= min_opr

        min_opr += 1
    return ops
