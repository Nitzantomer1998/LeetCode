import collections


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    """
    Finding the shortest path in a binary matrix, and return it
    Note : You are allowed to traverse only through cells with value of 0

    :param grid: Binary matrix
    :return: The shortest path in a binary matrix if exist, else -1

    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    # Edge case, if the starting cell or the end cell value is 1, then we don't have a clear path
    if grid[0][0] or grid[-1][-1]:
        return -1

    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW_COLUMN = len(grid)

    # Constants for the possible "next" path indices, for more readable code
    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # dequeue for bfs algorithm, Initialize with the starting indices and path length
    queue = collections.deque([(0, 0, 1)])

    # Updating cell value from 0 to 1, so we won't traverse him again
    grid[0][0] = 1

    # while loop for traverse each cell in the queue
    while queue:

        # Getting the data from the queue
        current_row, current_column, path_length = queue.popleft()

        # if we at cell target (grid[-1][-1]) than return the solution path length
        if current_row == current_column == MAX_ROW_COLUMN - 1:
            return path_length

        # Loop through all the possible neighbours for finding the best path
        for row_step, column_step in DIRECTIONS:

            # Setting the indices of the possible neighbors
            next_row = current_row + row_step
            next_column = current_column + column_step

            # if the next indices is valid and there's a clear path (cell value is 0) than add the cell to the queue
            if 0 <= next_row < MAX_ROW_COLUMN and 0 <= next_column < MAX_ROW_COLUMN:
                if grid[next_row][next_column] == 0:
                    # Adding the cell to the queue and Updating the value from 0 to 1, so we won't traverse him again
                    grid[next_row][next_column] = 1
                    queue.append((next_row, next_column, path_length + 1))

    # if we have reach to here, there's no a possible path than return -1 as default error
    return -1
