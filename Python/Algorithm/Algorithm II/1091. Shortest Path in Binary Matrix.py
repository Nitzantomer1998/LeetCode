import collections


class Solution:
    def is_valid_cell(self, row: int, column: int, ROWS: int, COLUMNS: int) -> bool:
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
        is_valid_row = row >= 0 and row < ROWS
        is_valid_column = column >= 0 and column < COLUMNS

        return is_valid_row and is_valid_column

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
            current_level = len(queue)

            for level in range(current_level):
                current_row, current_column, distance = queue.popleft()

                if current_row == ROWS - 1 and current_column == COLUMNS - 1:
                    return distance

                for row_step, column_step in DIRECTIONS:
                    next_row = current_row + row_step
                    next_column = current_column + column_step

                    if self.is_valid_cell(next_row, next_column, ROWS, COLUMNS):
                        if grid[next_row][next_column] == 0:
                            queue.append((next_row, next_column, distance + 1))
                            grid[next_row][next_column] = 1

        return -1
