def max_area_of_island(grid: list[list[int]]) -> int:
    
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    max_island_area = 0

    def island_area(row: int, column: int) -> int:
        
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or grid[row][column] == 0:
            return 0

        grid[row][column] = 0

        up = island_area(row + 1, column)
        down = island_area(row - 1, column)
        right = island_area(row, column + 1)
        left = island_area(row, column - 1)

        return 1 + up + down + right + left

    for row in range(len(grid)):
        for column in range(len(grid[0])):

            if grid[row][column] == 1:
                max_island_area = max(max_island_area, island_area(row, column))

    return max_island_area
