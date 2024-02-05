#!/usr/bin/python3
"""this docs contain function for Solution to the nqueens problem"""
import sys


def func_back(rl, nl, cls, ps, ng, brd):
    """func to backtrack to find solution"""
    if rl == nl:
        ress = []

        for x in range(len(brd)):
            for kk in range(len(brd[x])):
                if brd[x][kk] == 1:
                    ress.append([x, kk])

        print(ress)
        return

    for i in range(nl):
        if i in cls or (rl + i) in ps or (rl - i) in ng:
            continue

        cls.add(i)
        ps.add(rl + i)

        ng.add(rl - i)
        brd[rl][i] = 1

        func_back(rl+1, nl, cls, ps, ng, brd)

        cls.remove(i)
        ps.remove(rl + i)

        ng.remove(rl - i)
        brd[rl][i] = 0


def func_nqueens(nl):
    """func to solution to problems
    args:
        nl: the number of queens Must be 4
    return:
        result
    """
    cls = set()
    ps_dg = set()

    ng_dg = set()
    brd = [[0] * nl for x in range(nl)]

    func_back(0, nl, cls, ps_dg, ng_dg, brd)


if __name__ == "__main__":
    nl = sys.argv

    if len(nl) != 2:
        print("Usage: nqueens N")

        sys.exit(1)
    try:
        nx = int(nl[1])

        if nx < 4:
            print("N must be at least 4")
            sys.exit(1)

        func_nqueens(nx)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
