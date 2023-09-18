import collections


class Solution:
    def isValidCell(self, row: int, column: int, ROWS: int, COLUMNS: int) -> bool:
        """
        Check if a cell is valid within the grid.

        Args:
            row (int): The row index of the cell.
            column (int): The column index of the cell.
            ROWS (int): The total number of rows in the grid.
            COLUMNS (int): The total number of columns in the grid.

        Returns:
            bool: True if the cell is valid, False otherwise.
        """
        isValidRow = row >= 0 and row < ROWS
        isValidColumn = column >= 0 and column < COLUMNS

        return isValidRow and isValidColumn

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        Find the shortest path in a binary matrix from the top-left corner to the bottom-right corner.

        Args:
            grid (List[List[int]]): A 2D grid represented as a list of lists where 0 represents an empty cell and 1 represents an obstacle.

        Returns:
            int: The length of the shortest path from the top-left corner to the bottom-right corner, or -1 if no valid path exists.
        """
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        queue = collections.deque()

        if grid[0][0] == 0:
            queue.append((0, 0, 1))
            grid[0][0] = 1

        while queue:
            currentLevel = len(queue)

            for level in range(currentLevel):
                currentRow, currentColumn, distance = queue.popleft()

                if currentRow == ROWS - 1 and currentColumn == COLUMNS - 1:
                    return distance

                for rowStep, columnStep in DIRECTIONS:
                    nextRow = currentRow + rowStep
                    nextColumn = currentColumn + columnStep

                    if self.isValidCell(nextRow, nextColumn, ROWS, COLUMNS):
                        if grid[nextRow][nextColumn] == 0:
                            queue.append((nextRow, nextColumn, distance + 1))
                            grid[nextRow][nextColumn] = 1

        return -1
