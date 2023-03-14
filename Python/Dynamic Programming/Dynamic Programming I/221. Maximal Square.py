def maximal_square(matrix: list[list[str]]) -> int:
    """
    Given an m x n binary matrix filled with 0's and 1's, finds the largest square containing only 1's and returns its area.

    :param matrix: List of List of string represent 0 or 1
    :return: The area of the largest square seen

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Check for edge case of empty matrix
    if not matrix:
        return 0

    # Get the number of rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])

    # Initialize a 2D table to store the size of the largest square that can be formed at each cell in the matrix
    max_square_size = [[0] * cols for _ in range(rows)]

    # Initialize the max size of the square to be 0
    max_size = 0

    # Traverse through the matrix and fill in the max_square_size table
    for i in range(rows):
        for j in range(cols):
            # If the cell value is 0, no square can be formed, set max_square_size value to 0
            if matrix[i][j] == '0':
                max_square_size[i][j] = 0

            else:
                # If the cell value is 1, we can form a square with this cell as the bottom right corner
                # The size of the square is determined by the minimum size of squares that can be formed by
                # extending the squares at its top, left, and top-left corner by 1
                if i == 0 or j == 0:
                    # If this is the first row or first column, the maximum size square that can be formed is 1
                    max_square_size[i][j] = 1

                else:
                    # Otherwise, we take the minimum size of squares that can be formed by extending the squares
                    # at the top, left, and top-left corner by 1, and add 1 to it to form a new square
                    max_square_size[i][j] = min(max_square_size[i - 1][j], max_square_size[i][j - 1],
                                                max_square_size[i - 1][j - 1]) + 1

                # Update the max size of the square seen so far
                max_size = max(max_size, max_square_size[i][j])

    # Return the area of the largest square seen
    return max_size * max_size
