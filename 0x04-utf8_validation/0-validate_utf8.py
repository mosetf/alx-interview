#!/usr/bin/python3
"""
This script validates whether a given list of
integers represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if the given data represents a valid UTF-8 encoding.

    Args:
        data (list[int]): The data to be checked.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    bytes_to_process = 0

    for num in data:
        # Get the binary representation of the least significant 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if bytes_to_process == 0:
            for bit in bin_rep:
                if bit == '0' : break
                bytes_to_process += 1

            if bytes_to_process == 0:
                continue
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        bytes_to_process -= 1

    return bytes_to_process == 0
