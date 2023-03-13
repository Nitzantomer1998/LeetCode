def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    
    nth_unique_paths = [[0] * len(obstacle_grid[0]) for _ in range(len(obstacle_grid))]
    nth_unique_paths[0][0] = 1  # There is only one way to reach the starting position

    for column in range(1, len(obstacle_grid[0])):
        if obstacle_grid[0][column] == 0 and nth_unique_paths[0][column - 1] != 0:
            nth_unique_paths[0][
                column] = 1

    for row in range(1, len(obstacle_grid)):
        if obstacle_grid[row][0] == 0 and nth_unique_paths[row - 1][0] != 0:
            nth_unique_paths[row][
                0] = 1

    for row in range(1, len(obstacle_grid)):
        for column in range(1, len(obstacle_grid[0])):
            if obstacle_grid[row][column] == 0:
               
                nth_unique_paths[row][column] = nth_unique_paths[row - 1][column] + nth_unique_paths[row][column - 1]

    return 0 if obstacle_grid[0][0] or obstacle_grid[-1][-1] else nth_unique_paths[-1][-1]
