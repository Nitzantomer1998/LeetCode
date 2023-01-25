import collections


def update_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Updating each cell in matrix to be the distance of the nearest 0, and return it

    :param matrix: Binary matrix
    :return: The updated matrix with each cell storing the distance of the nearest 0

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries and possible indices increased, for more readable code
    MAX_ROW = len(matrix)
    MAX_COLUMN = len(matrix[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # dequeue for bfs algorithm, Initialize with the root of the tree
    queue = collections.deque()

    # Double loop to traverse the matrix
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            # if the cell value is 0, then add it to the queue
            # Note: We add the 0 value cells to the queue first, cause distance counter start from 0 value cells
            if matrix[row][column] == 0:
                queue.append([row, column])

            # if the cell value is not 0, then give it special value. symbol for unvisited cell
            else:
                matrix[row][column] = -1

    # Loop to traverse the queue as long there's items in
    while queue:

        # Unpacking the list indices of the first item in the queue
        row, column = queue.popleft()

        # Iterative loop to get the 4 possible cell directions
        for row_step, column_step in DIRECTIONS:

            # Storing the new row and column indices check
            new_row = row + row_step
            new_column = column + column_step

            # if the new indices is out of boundaries, continue to the next iteration
            if not (0 <= new_row < MAX_ROW and 0 <= new_column < MAX_COLUMN):
                continue

            # if the new indices were already visited, continue to the next iteration
            # Note: -1 is a defined symbol for not visited cell
            if matrix[new_row][new_column] != -1:
                continue

            # Update matrix "new" cell value to the found one, and add it to the queue
            matrix[new_row][new_column] = matrix[row][column] + 1
            queue.append([new_row, new_column])

    # Returning the modified matrix
    return matrix
