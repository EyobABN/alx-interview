#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    """ Returns true if all boxes can be unlocked as per rules """
    numberOfBoxes = len(boxes)
    expectedKeys = []
    foundKeys = []
    for i in range(1, numberOfBoxes):
        expectedKeys.append(i)
    for boxNumber, box in enumerate(boxes):
        for key in box:
            if (key != boxNumber
                    and key in expectedKeys
                    and key not in foundKeys):
                foundKeys.append(key)
    foundKeys = sorted(foundKeys)
    if (foundKeys == expectedKeys):
        return True
    return False
