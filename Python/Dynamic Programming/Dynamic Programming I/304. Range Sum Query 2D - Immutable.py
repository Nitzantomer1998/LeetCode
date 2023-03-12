class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        """
        Initializes the NumMatrix object with the input matrix.

        :param matrix: A 2D list of integers representing the matrix.

        Time Complexity: o(n * m)
        Space Complexity: o(n * m)
        """
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        # Calculate the prefix sum matrix using dynamic programming.
        # The value at position (i,j) represents the sum of all elements
        # in the sub-matrix from (0,0) to (i,j) in the original matrix.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = matrix[i - 1][j - 1] + self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] - \
                                        self.prefix_sum[i - 1][j - 1]

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Calculates the sum of elements inside a rectangle defined by the
        input coordinates (row1, col1) and (row2, col2) using the prefix
        sum matrix.


        :param row1: An integer representing the row index of the upper left corner.
        :param col1: An integer representing the column index of the upper left corner.
        :param row2: An integer representing the row index of the lower right corner.
        :param col2: An integer representing the column index of the lower right corner.
        :return: An integer representing the sum of the elements inside the rectangle.

        Time Complexity: o(1)
        Space Complexity: o(1)
        """
        # Calculate the sum of the sub-matrix from (0,0) to (row2, col2)
        # and subtract the overlapping sub-matrices to get the sum of the
        # elements inside the rectangle.
        return self.prefix_sum[row2 + 1][col2 + 1] - self.prefix_sum[row1][col2 + 1] - self.prefix_sum[row2 + 1][col1] + \
            self.prefix_sum[row1][col1]
