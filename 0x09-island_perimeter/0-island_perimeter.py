#!/usr/bin/python3
"""this docs contain Define island_perimeter function
that finds the perimeter of an island in a body of water"""

bd_4 = set()
bd_3 = set()

bd_2 = set()
bd_1 = set()


def func_bdy(grid, x, k):
    """func to Find cells with either exposed boundar
    args:
        grid: the 2d list
        x: row number
        k: column number
    return:
        Nothing
    """
    bds = 0

    try:
        if x == 0:
            bds += 1
        elif grid[x-1][k] == 0:
            bds += 1
    except Exception:
        bds += 1

    try:
        if grid[x+1][k] == 0:
            bds += 1
    except Exception:
        bds += 1

    try:
        if grid[x][k+1] == 0:
            bds += 1
    except Exception:
        bds += 1

    try:
        if k == 0:
            bds += 1
        elif grid[x][k-1] == 0:
            bds += 1

    except Exception:
        bds += 1

    if bds == 1:
        bd_1.add((x, k))

    elif bds == 2:
        bd_2.add((x, k))

    elif bds == 3:
        bd_3.add((x, k))

    elif bds == 4:
        bd_4.add((x, k))


def island_perimeter(grid):
    """this func to Calculate and return perimeter of island
    in the grid Grid is a rectangular grid where 0s represent water
    1s represent land Each cell is a square with a side length of 1
    args:
        grid: the 2d list of ints either 0 or 1
    return:
        return the perimeter of island
    """

    if grid == []:
        return 0

    leng = len(grid)
    wedth = len(grid[0])

    for x in range(leng):
        for k in range(wedth):
            if grid[x][k] == 1:
                func_bdy(grid, x, k)

                if len(bd_4) != 0:
                    return 4

    pmr = (len(bd_3) * 3) + (len(bd_2) * 2) + (len(bd_1))

    return pmr
