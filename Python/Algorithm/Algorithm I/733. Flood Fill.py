import collections
from typing import List


class Solution:
    def isValidCell(self, row: int, column: int, ROWS: int, COLUMNS: int) -> bool:
        """
        Check if the given cell coordinates are within the bounds of the grid.

        Args
            row (int): Row index of the cell.
            column (int): Column index of the cell.
            ROWS (int): Total number of rows in the grid.
            COLUMNS (int): Total number of columns in the grid.

        Returns
            bool: True if the cell is valid, False otherwise.

        Time Complexity: o(1) since we do 2 comparisons.
        Space Complexity: o(1) since we do not use any extra space.
        """
        isValidRow = 0 <= row < ROWS
        isValidColumn = 0 <= column < COLUMNS

        return isValidRow and isValidColumn

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Perform flood fill on the given image starting from the specified coordinates.

        Args
            image (List[List[int]]): The 2D grid representing the image.
            sr (int): The starting row index for flood fill.
            sc (int): The starting column index for flood fill.
            color (int): The new color to be filled.

        Returns
            List[List[int]]: The modified image after flood fill.

        Time Complexity: o(m * n), where m is the number of rows and n is the number of columns in the image.
        Space Complexity: o(m * n), where m is the number of rows and n is the number of columns in the image.
        """
        ROWS = len(image)
        COLUMNS = len(image[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        oldColor = image[sr][sc]
        newColor = color

        if oldColor == newColor:
            return image

        queue = collections.deque([[sr, sc]])
        image[sr][sc] = newColor

        while queue and queue[0]:
            row, column = queue.popleft()
            
            for rowStep, columnStep in DIRECTIONS:
                newRow = row + rowStep
                newColumn = column + columnStep

                if not self.isValidCell(newRow, newColumn, ROWS, COLUMNS):
                    continue

                if image[newRow][newColumn] != oldColor:
                    continue

                image[newRow][newColumn] = newColor
                queue.append([newRow, newColumn])

        return image
