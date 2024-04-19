class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandsCounter = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == '1':
                    self.DFS(grid, row, column)
                    islandsCounter += 1

        return islandsCounter

    def DFS(self, grid: List[List[str]], row: int, column: int) -> None:
        if not (0 <= row < len(grid) and 0 <= column < len(grid[row])):
            return

        if grid[row][column] == '0':
            return

        grid[row][column] = '0'
        self.DFS(grid, row - 1, column)
        self.DFS(grid, row + 1, column)
        self.DFS(grid, row, column - 1)
        self.DFS(grid, row, column + 1)
