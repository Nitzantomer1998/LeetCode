import collections


def update_matrix(matrix: list[list[int]]) -> list[list[int]]:
    
    MAX_ROW = len(matrix)
    MAX_COLUMN = len(matrix[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = collections.deque()

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            
            if matrix[row][column] == 0:
                queue.append([row, column])

            else:
                matrix[row][column] = -1

    while queue:

        row, column = queue.popleft()

        for row_step, column_step in DIRECTIONS:

            new_row = row + row_step
            new_column = column + column_step

            if not (0 <= new_row < MAX_ROW and 0 <= new_column < MAX_COLUMN):
                continue

            if matrix[new_row][new_column] != -1:
                continue

            matrix[new_row][new_column] = matrix[row][column] + 1
            queue.append([new_row, new_column])

    return matrix
