def generate(num_rows: int) -> list[list[int]]:
    """
    Generate the first num_rows of Pascal's triangle.

    :param num_rows: an integer representing the number of rows to generate.
    :return: The list of the first num_rows of Pascal triangle

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n ^ 2)
    """
    # Initialize the result list with the first num_rows rows of Pascal's triangle.
    pascal_triangle = [[1] * (i + 1) for i in range(num_rows)]

    # Compute the remaining elements of Pascal's triangle.
    for row in range(2, num_rows):
        for col in range(1, row):
            # Each element of Pascal's triangle is the sum of the two elements directly above it.
            pascal_triangle[row][col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]

    # Returning the list of the first num_rows of Pascal triangle
    return pascal_triangle
