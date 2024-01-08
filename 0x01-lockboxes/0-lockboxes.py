#!/usr/bin/python3
"""defines a func that determines if box contains list"""


def canUnlockAll(boxes):
    """func to define if box unlocked"""
    pos = 0
    unlock = {}

    for box in boxes:
        if len(box) == 0 or pos == 0:
            unlock[pos] = "always_unlocked"

        for k in box:
            if k < len(boxes) and k != pos:
                unlock[k] = k
        if len(unlock) == len(boxes):
            return True
        pos += 1
    return False
