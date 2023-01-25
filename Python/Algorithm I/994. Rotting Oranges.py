def oranges_rotting(grid: list[list[int]]) -> int:
   
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rotten_queue = []

    fresh_counter = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):

            if grid[row][column] == 2:
                rotten_queue.append((row, column))

            elif grid[row][column] == 1:
                fresh_counter += 1

    minutes_passed = 0

    while rotten_queue and fresh_counter:

        minutes_passed += 1

        for _ in range(len(rotten_queue)):

            row, column = rotten_queue.pop(0)

            for direction in DIRECTIONS:

                new_row = row + direction[0]
                new_column = column + direction[1]

                if not (0 <= new_row < MAX_ROW and 0 <= new_column < MAX_COLUMN):
                    continue

                if grid[new_row][new_column] != 1:
                    continue

                grid[new_row][new_column] = 2

                fresh_counter -= 1

                rotten_queue.append((new_row, new_column))

    return minutes_passed if fresh_counter == 0 else -1
