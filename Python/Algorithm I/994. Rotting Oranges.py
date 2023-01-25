def oranges_rotting(grid: list[list[int]]) -> int:
    """
    Update the orange grid, such every minute a rotten orange rotten a fresh orange that is in his 4 direction
    return the amount of minutes its take if possible, else -1

    :param grid: Matrix representing rotten and fresh oranges
    :return: The amount of minutes its took for the grid to be rotten if possible, else -1

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries and possible indices increased, for more readable code
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # List used as queue for the rotten oranges
    rotten_queue = []

    # Counter for the fresh oranges in the grid
    fresh_counter = 0

    # Double loop to traverse the grid
    for row in range(len(grid)):
        for column in range(len(grid[0])):

            # if the cell value is 2, then add it to the rotten queue
            # Note: We add the 2 value cells to the queue, because they will impact fresh ones (1 value cells)
            if grid[row][column] == 2:
                rotten_queue.append((row, column))

            # if the cell value is 1, then update the fresh oranges counter
            elif grid[row][column] == 1:
                fresh_counter += 1

    # Counter for the amount of minutes passed till all the grid is rotten
    minutes_passed = 0

    # Loop to traverse the rotten queue as long there's items in, and as long there's fresh oranges
    while rotten_queue and fresh_counter:

        # Update the minutes amounts its take to the grid became rotten
        minutes_passed += 1

        # Double Loop to update the current fresh oranges that's should turn rotten
        for _ in range(len(rotten_queue)):

            # Getting the first rotten cell indices
            row, column = rotten_queue.pop(0)

            for direction in DIRECTIONS:

                # Storing the new row and column indices check
                new_row = row + direction[0]
                new_column = column + direction[1]

                # if the new indices is out of boundaries, continue to the next iteration
                if not (0 <= new_row < MAX_ROW and 0 <= new_column < MAX_COLUMN):
                    continue

                # if the new indices value is other than 1, continue to the next iteration because nothing would change
                if grid[new_row][new_column] != 1:
                    continue

                # Update new rotten orange in the grid
                grid[new_row][new_column] = 2

                # Update the fresh orange counter
                fresh_counter -= 1

                # Adding the new rotten orange to the rotten queue
                rotten_queue.append((new_row, new_column))

    # Returning the amount of minutes passed till all the grid is rotten if possible, else -1 ("Failed")
    return minutes_passed if fresh_counter == 0 else -1
