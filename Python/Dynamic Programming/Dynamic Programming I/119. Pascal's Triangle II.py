def get_row(row_index: int) -> list[int]:
    """
    Generate the row_index of Pascal's triangle.

    :param row_index: an integer representing the row number to generate.
    :return: The row list of the row row_index of Pascal triangle

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n ^ 2)
    """
    # Initialize the result list with row_index rows of Pascal's triangle.
    pascal_triangle = [[1] * (i + 1) for i in range(row_index + 1)]

    # Compute the remaining elements of Pascal's triangle.
    for row in range(2, row_index + 1):
        for col in range(1, row):
            # Each element of Pascal's triangle is the sum of the two elements directly above it.
            pascal_triangle[row][col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]

    # Returning The row list of the row row_index of Pascal triangle
    return pascal_triangle[-1]
