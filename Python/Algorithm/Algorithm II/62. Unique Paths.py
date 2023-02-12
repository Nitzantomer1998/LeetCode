def unique_paths(m: int, n: int) -> int:
    """
    Finding the amount of paths we have from start ([0][0]) to the end ([m - 1][n - 1]), and return it
    Note : From each cell you allowed to forward only in the directions right / down

    :param m: Integer represent the number of rows in a matrix
    :param n: Integer represent the number of column in a matrix
    :return: The amount of paths we have from start ([0][0]) to the end ([m - 1][n - 1])

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Initialize M x N nth_unique_paths, each cell describe the amount of ways we can get to him, basic case value is 1
    nth_unique_paths = [[1 for _ in range(n)] for _ in range(m)]

    # Double loop to traverse each cell and update the amount of ways we can get to him
    for row in range(1, m):
        for column in range(1, n):
            nth_unique_paths[row][column] = nth_unique_paths[row - 1][column] + nth_unique_paths[row][column - 1]

    # Returning the amount of ways we can get from start to end
    return nth_unique_paths[-1][-1]
