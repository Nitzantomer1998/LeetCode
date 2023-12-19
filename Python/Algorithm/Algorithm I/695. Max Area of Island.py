import collections
from typing import List


class Solution:
    def isValidCell(self, row: int, column: int, ROWS: int, COLUMNS: int) -> bool:
        """
        Checks if the given cell coordinates are valid within the grid.

        Args:
            row: The row index of the cell.
            column: The column index of the cell.
            ROWS: The total number of rows in the grid.
            COLUMNS: The total number of columns in the grid.

        Returns:
            True if the cell is valid, False otherwise.

        Time Complexity: o(1) since we do 2 comparisons.
        Space Complexity: o(n) since we do not use any extra space.
        """
        isValidRow = 0 <= row < ROWS
        isValidColumn = 0 <= column < COLUMNS

        return isValidRow and isValidColumn

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum area of an island in the binary matrix.

        Args:
            grid: The binary matrix representing land (1) and water (0).

        Returns:
            The maximum area of an island. If there is no island, returns 0.

        Time Complexity: o(m * n), where m is the number of rows and n is the number of columns in the grid.
        Space Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
        """
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        maxArea = 0

        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column]:
                    grid[row][column] = 0

                    queue = collections.deque()
                    queue.append((row, column))
                    currentArea = 1

                    while queue and queue[0]:
                        row, column = queue.popleft()

                        for rowStep, columnStep in DIRECTIONS:
                            newRow = row + rowStep
                            newColumn = column + columnStep

                            if self.isValidCell(newRow, newColumn, ROWS, COLUMNS):
                                if grid[newRow][newColumn]:
                                    queue.append((newRow, newColumn))
                                    grid[newRow][newColumn] = 0
                                    currentArea += 1

                    maxArea = max(maxArea, currentArea)

        return maxArea
