def num_islands(grid: list[list[str]]) -> int:
    """
    Finding the amount of islands in grid, and return its area

    :param grid: Matrix of integers, represent island if 1, 0 if water
    :return: The amount of islands in grid

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    # Integer counter for storing the amount of existing islands
    island_counter = 0

    # Assisting function to make the DFS calls
    def map_island(row, column) -> None:
        """
        Recursive function for checking if the current indices indicate an island using DFS Algorithm

        :param row: Integer represent the current cell row
        :param column: Integer represent the current cell column
        :return: None, Everything happen in place
        """
        # if the sent indices are invalid or the cell is not part of the island, return
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or grid[row][column] == '0':
            return

        # Updating cell value from 1 to 0, so we won't traverse him again
        grid[row][column] = '0'

        # callback to the other 4 directions to continue mapping the current island (might be bigger)
        map_island(row + 1, column)
        map_island(row - 1, column)
        map_island(row, column - 1)
        map_island(row, column + 1)

        # Return nothing, means we mapped the current island
        return

    # Double loop to traverse every cell in the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):

            # if we found an island, make a callback for mapping the island, and updating the island counter
            if grid[row][column] == '1':
                map_island(row, column)
                island_counter += 1

    # Returning the amount of existing islands
    return island_counter
