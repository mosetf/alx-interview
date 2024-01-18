#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """Method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if n <= 1:
        return 0

    num = 2
    operations = 0

    while num <= n:
        if n % num == 0:
            operations += num
            n = n / num
        else:
            num += 1

    return operations
