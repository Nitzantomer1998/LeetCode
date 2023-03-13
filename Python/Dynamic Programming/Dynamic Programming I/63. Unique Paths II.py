def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    """
    Finding the amount of paths we have from start ([0][0]) to the end ([m - 1][n - 1]), and return it
    Note : From each cell you allowed to forward only in the directions right / down, and cant traverse obstacles

    :param obstacle_grid: An m x n integer array representing a grid with obstacles and empty spaces.
    :return: The number of unique paths from the top-left corner to the bottom-right corner, without passing through obstacles.

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Initialize a 2D array to store the number of unique paths from the top-left corner to each position
    # nth_unique_paths[i][j] represents the number of unique paths from the top-left corner to position (i,j)
    nth_unique_paths = [[0] * len(obstacle_grid[0]) for _ in range(len(obstacle_grid))]
    nth_unique_paths[0][0] = 1  # There is only one way to reach the starting position

    # Fill the first row of nth_unique_paths
    for column in range(1, len(obstacle_grid[0])):
        if obstacle_grid[0][column] == 0 and nth_unique_paths[0][column - 1] != 0:
            nth_unique_paths[0][
                column] = 1  # If there is no obstacle and the previous cell in the same row is reachable, there is one path

    # Fill the first column of nth_unique_paths
    for row in range(1, len(obstacle_grid)):
        if obstacle_grid[row][0] == 0 and nth_unique_paths[row - 1][0] != 0:
            nth_unique_paths[row][
                0] = 1  # If there is no obstacle and the previous cell in the same column is reachable, there is one path

    # Fill the remaining cells of nth_unique_paths
    for row in range(1, len(obstacle_grid)):
        for column in range(1, len(obstacle_grid[0])):
            if obstacle_grid[row][column] == 0:
                # If there is no obstacle at the current position, the number of unique paths from the top-left corner to this
                # position is the sum of the number of unique paths from the top-left corner to the previous positions in the
                # same row and column.
                nth_unique_paths[row][column] = nth_unique_paths[row - 1][column] + nth_unique_paths[row][column - 1]

    # Return the number of unique paths to the bottom-right corner
    return 0 if obstacle_grid[0][0] or obstacle_grid[-1][-1] else nth_unique_paths[-1][-1]
