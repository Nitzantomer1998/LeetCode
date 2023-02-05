def num_islands(grid: list[list[str]]) -> int:
    
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    island_counter = 0

    def map_island(row, column) -> None:
        
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or grid[row][column] == '0':
            return

        grid[row][column] = '0'

        map_island(row + 1, column)
        map_island(row - 1, column)
        map_island(row, column - 1)
        map_island(row, column + 1)

        return

    for row in range(len(grid)):
        for column in range(len(grid[row])):

            if grid[row][column] == '1':
                map_island(row, column)
                island_counter += 1

    return island_counter
