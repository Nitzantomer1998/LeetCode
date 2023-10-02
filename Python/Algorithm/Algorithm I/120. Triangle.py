from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Find the minimum path sum from top to bottom in a triangle.

        Args:
            triangle (List[List[int]]): A list of lists representing the triangle.

        Returns:
            int: The minimum path sum.

        Time Complexity: o(n) where n is the number of elements in the triangle.
        Space Complexity: o(1)
        """
        ROWS = len(triangle)

        for row in range(ROWS - 2, -1, -1):
            COLUMNS = len(triangle[row])

            for column in range(COLUMNS):
                firstOption = triangle[row + 1][column]
                secondOption = triangle[row + 1][column + 1]

                triangle[row][column] += min(firstOption, secondOption)

        return triangle[0][0]
