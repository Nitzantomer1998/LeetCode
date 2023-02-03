def max_area_of_island(grid: list[list[int]]) -> int:
    """
    Finding the maximum island area in grid, and return its area

    :param grid: Matrix of integers, represent island if 1, 0 if water
    :return: The maximum island area in grid

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    # Variable to store the solution
    max_island_area = 0

    # Assisting function to make the DFS calls
    def island_area(row: int, column: int) -> int:
        """
        Recursive function for finding the current island area using DFS Algorithm

        :param row: Integer represent the current cell row
        :param column: Integer represent the current cell column
        :return: The current island area
        """
        # if the sent indices are invalid or the cell is not part of the island, return 0
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or grid[row][column] == 0:
            return 0

        # we're changing the cell value from 1 to 0, so we won't count him again
        grid[row][column] = 0

        # callback to the other 4 directions for a possible island
        up = island_area(row + 1, column)
        down = island_area(row - 1, column)
        right = island_area(row, column + 1)
        left = island_area(row, column - 1)

        # Return the current island area
        return 1 + up + down + right + left

    # Double loop to traverse every cell in the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):

            # if we found an island, make a callback for mapping the island, and updating the max island area
            if grid[row][column] == 1:
                max_island_area = max(max_island_area, island_area(row, column))

    # Returning the solution
    return max_island_area
