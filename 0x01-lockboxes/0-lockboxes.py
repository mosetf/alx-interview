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
                      and contains indexes of other boxes that can be unlocked.

    Returns:
        bool: True if all boxes can be unlocked otherwise false
    """
    x = len(boxes)

    if x == 0:
       return False  # If there are no boxes, retur false

    visited_index = [False] * x  # Initialize a list to track visited indices
    stack = [0]  # Start with the first box (index 0)

    while stack:
        current_index = stack.pop()
        visited_index[current_index] = True

        current_array = boxes[current_index]

        for value in current_array:
            if 0 <= value < x and not visited_index[value]:
                stack.append(value)

    return all(visited_index)
