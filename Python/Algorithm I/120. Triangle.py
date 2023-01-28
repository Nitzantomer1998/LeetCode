def minimum_total(triangle: list[list[int]]) -> int:
    """
    Finding the minimum path sum from top to bottom of a triangle array, and return it
    Note: From each [row][column] you may proceed by going [row + 1][column] or [row + 1][column + 1]

    :param triangle: List of List of integers
    :return: The minimum path sum from top to bottom of a triangle array

    Time Complexity: o(n^2)
    Space Complexity: o(1)
    """
    # Loop to start from the bottom of the triangle and moving up
    for row in reversed(range(len(triangle))):

        # Loop to traverse the indices of the current row
        for column in range(len(triangle[row]) - 1):
            # Variables to store the calculation of the two option to get to triangle[row - 1][column]
            first_option = triangle[row - 1][column] + triangle[row][column]
            second_option = triangle[row - 1][column] + triangle[row][column + 1]

            # Updating the triangle[row - 1][column] value to be the minimum sum to get to him
            triangle[row - 1][column] = min(first_option, second_option)

    # Returning the minimum sum to get from top to bottom
    return triangle[0][0]
