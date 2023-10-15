import collections
from typing import List


class Solution:
    def isValidCell(self, ROWS: int, COLUMNS: int, row: int, column: int) -> bool:
        """
        Checks if a given cell is within the bounds of the matrix.

        Args:
            ROWS: The number of rows in the matrix.
            COLUMNS: The number of columns in the matrix.
            row: The row of the cell to check.
            column: The column of the cell to check.

        Returns:
            True if the cell is within the bounds of the matrix, False otherwise.

        Time Complexity: o(1) since we are only make a 4 comparisons.
        Space Complexity: o(1) since we are not using any extra space.
        """
        isValidRow = 0 <= row < ROWS
        isValidColumn = 0 <= column < COLUMNS

        return isValidRow and isValidColumn

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Updates a matrix such that each cell contains the minimum number of moves required to reach a cell
        containing 0.

        Args:
            mat: A list of lists of integers, representing the matrix to update.

        Returns:
            A list of lists of integers, representing the updated matrix.

        Time Complexity: o(m * n) where m is the number of rows and n is the number of columns in the matrix.
        Space Complexity: o(m * n) where m is the number of rows and n is the number of columns in the matrix.
        """
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS = len(mat)
        COLUMNS = len(mat[0])

        queue = collections.deque()
        for row in range(ROWS):
            for column in range(COLUMNS):
                if mat[row][column] == 0:
                    queue.append([row, column])

                else:
                    mat[row][column] = -1

        while queue and queue[0]:
            row, column = queue.popleft()

            for rowStep, columnStep in DIRECTIONS:
                newRow = row + rowStep
                newColumn = column + columnStep

                if not self.isValidCell(ROWS, COLUMNS, newRow, newColumn) or mat[newRow][newColumn] != -1:
                    continue

                mat[newRow][newColumn] = mat[row][column] + 1
                queue.append([newRow, newColumn])

        return mat

