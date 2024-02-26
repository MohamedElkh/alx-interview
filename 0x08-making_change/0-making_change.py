#!/usr/bin/python3
"""this docs contain function making change"""


def makeChange(coins, total):
    """
    this function to  minimum number of coins
    args:
        coins: list of coins of different values
        total: the total value to be met
    return:
        Num of coins or -1 if meeting the total
    """

    if total <= 0:
        return 0

    if coins == [] or coins is None:
        return -1

    try:
        num = coins.index(total)
        return 1

    except ValueError:
        pass

    coins.sort(reverse=True)

    coin_c = 0

    for x in coins:
        if total % x == 0:
            coin_c += int(total / x)
            return coin_c

        if total - x >= 0:
            if int(total / x) > 1:
                coin_c += int(total / x)

                total = total % x
            else:
                coin_c += 1
                total -= x

                if total == 0:
                    break

    if total > 0:
        return -1

    return coin_c
