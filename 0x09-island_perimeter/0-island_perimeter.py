#!/usr/bin/python3
"""Module for island perimeter
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island defined by a grid of 1's.

    Args:
        grid (List[List[int]]): A 2D list of integers representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Check North neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1

                # Check South neighbor
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1

                # Check West neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

                # Check East neighbor
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
