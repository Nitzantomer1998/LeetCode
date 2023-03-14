import sys


def min_path_sum(grid: list[list[int]]) -> int:
    """
    Given an m x n grid filled with non-negative numbers, finds a path from top left to bottom right,
    which minimizes the sum of all numbers along its path.

    :param grid: The input grid.
    :return: The minimum sum of numbers along a path from top left to bottom right in the grid.

    Time Complexity: o(n * m)
    Space Complexity: o(1)
    """
    # Get the number of rows and columns in the grid
    rows, columns = len(grid), len(grid[0])

    # Double loop to traverse each cell and update the minimum path sum
    for row in range(rows):
        for column in range(columns):
            # Check if we're at the start cell (top left)
            if row == column == 0:
                continue

            else:
                # Compute the minimum path sum to the current cell
                top_path = grid[row - 1][column] if row > 0 else sys.maxsize
                left_path = grid[row][column - 1] if column > 0 else sys.maxsize
                grid[row][column] += min(top_path, left_path)

    # Return the minimum path sum to the bottom right cell
    return grid[-1][-1]
