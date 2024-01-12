#!/usr/bin/python3
"""
method to unlock boxes
"""


def canUnlockAll(boxes):
    """
    A method that checks if all boxes can be opened
    """
    bool_list = [True]
    for i in range(1, len(boxes)):
        for n, box in enumerate(boxes):
            if n != i and len(box) > 0:
                if i in box:
                    bool_list.append(True)
                    break
        else:
            bool_list.append(False)
    return all(bool_list)
