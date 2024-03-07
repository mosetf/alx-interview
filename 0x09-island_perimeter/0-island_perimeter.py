#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island,
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    p = 0
    if type(grid) != list:
        return 0
    s = len(grid)
    for j, row in enumerate(grid):
        n = len(row)
        for i, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                j == 0 or (len(grid[j - 1]) > i and grid[j - 1][i] == 0),
                i == n - 1 or (n > i + 1 and row[i + 1] == 0),
                j == s - 1 or (len(grid[j + 1]) > i and grid[j + 1][i] == 0),
                i == 0 or row[i - 1] == 0,
            )
            p += sum(edges)
        return p
