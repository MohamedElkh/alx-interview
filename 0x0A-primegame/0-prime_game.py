#!/usr/bin/python3
"""this docs conatin two functions to define isWineer function,
a solution to the Prime Game problem.
"""


def func_pri(n):
    """this func to return the list of prime numbers
    args:
        n: upper boundary of range. lower boundary
    """
    prix = []
    svx = [True] * (n + 1)

    for xl in range(2, n + 1):
        if (svx[xl]):
            prix.append(xl)

            for y in range(xl, n + 1, xl):
                svx[y] = False
    return prix


def isWinner(x, nums):
    """this func to determines winner of Prime Game
    args:
        x: the no. of rounds of game
        nums: the upper limit of range for each round
    return:
        the name of winner or  None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    Maria = Ben = 0

    for y in range(x):
        prix = func_pri(nums[y])

        if len(prix) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'

    return None
