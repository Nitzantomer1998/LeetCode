import collections


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    
    if grid[0][0] or grid[-1][-1]:
        return -1

    MAX_ROW_COLUMN = len(grid)

    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    queue = collections.deque([(0, 0, 1)])

    grid[0][0] = 1

    while queue:

        current_row, current_column, path_length = queue.popleft()

        if current_row == current_column == MAX_ROW_COLUMN - 1:
            return path_length

        for row_step, column_step in DIRECTIONS:

            next_row = current_row + row_step
            next_column = current_column + column_step

            if 0 <= next_row < MAX_ROW_COLUMN and 0 <= next_column < MAX_ROW_COLUMN:
                if grid[next_row][next_column] == 0:
                    grid[next_row][next_column] = 1
                    queue.append((next_row, next_column, path_length + 1))

    return -1
