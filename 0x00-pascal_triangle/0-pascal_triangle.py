#!/usr/bin/python3
"""this a module for Pascal's triangl"""


def pascal_triangle(n):
    """func to create a list of lists of int"""
    tri = []
    if type(n) is not int or n <= 0:
        return tri
    for x in range(n):
        li = []
        for k in range(x + 1):
            if k == 0 or k == x:
                li.append(1)
            elif x > 0 and k > 0:
                li.append(tri[x - 1][k - 1] + tri[x - 1][k])
        tri.append(li)
    return tri
