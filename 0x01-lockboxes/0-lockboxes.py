#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""

""" LOGIC:
This implementation keeps track of two sets: `keyRing`, which contains
the keys that have been obtained so far, and `unlockedBoxes`, which contains
the indices of the boxes that have been unlocked so far. The function then
loops until no more boxes can be unlocked, trying to unlock any box that
has not been unlocked yet and for which the key is available.

"""


def canUnlockAll(boxes):
    """keyRing initialized with the contents of the first sublist in `boxes`
    (already unlocked), `unlockedBoxes` initialized with the value 0,
    representing the first box that is already unlocked"""
    keyRing = set(boxes[0])
    unlockedBoxes = {0}

    """loop until no more boxes can be unlocked (`break`)"""
    while True:
        """how many boxes have been unlocked in this iteration?"""
        b_unlocked = 0
        """try to unlock remaining boxes"""
        for i in range(len(boxes)):
            if i not in unlockedBoxes and i in keyRing:
                unlockedBoxes.add(i)
                keyRing.update(boxes[i])
                b_unlocked += 1
        """if no boxes were unlocked, we're done"""
        if b_unlocked == 0:
            break

    """check if all boxes were unlocked"""
    return len(unlockedBoxes) == len(boxes)
