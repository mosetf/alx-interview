#!/usr/bin/python3
"""
function that checks if you can unlock all
the boxes based on their indices
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked starting from the first box.

    Args:
        boxes (list): A list of lists where each inner list represents a box
                      and contains indices of other boxes that can be unlocked.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    if boxes:
        numOfBoxes = len(boxes)
        setOfKeys = {0}
        setOfKeys.update(boxes[0])
        visitedBoxes = {0}

        while True:
            newBoxVisited = False
            keys = setOfKeys.copy()

            for key in keys:
                if key not in visitedBoxes and key < numOfBoxes:
                    setOfKeys.update(boxes[key])
                    visitedBoxes.add(key)
                    newBoxVisited = True

            if not newBoxVisited:
                break

        for n in range(numOfBoxes):
            if n not in setOfKeys:
                return False

        return True

    return False
