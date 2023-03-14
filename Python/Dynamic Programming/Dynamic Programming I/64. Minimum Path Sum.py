import sys


def min_path_sum(grid: list[list[int]]) -> int:
    
    rows, columns = len(grid), len(grid[0])

    for row in range(rows):
        for column in range(columns):
            if row == column == 0:
                continue

            else:
                top_path = grid[row - 1][column] if row > 0 else sys.maxsize
                left_path = grid[row][column - 1] if column > 0 else sys.maxsize
                grid[row][column] += min(top_path, left_path)

    return grid[-1][-1]
