function dfs(grid: number[][], row: number, column: number): number {
    if (row >= 0 && column >= 0 && row < grid.length && column < grid[0].length) {
        if (grid[row][column]) {
            grid[row][column] = 0;

            const upCell: number = dfs(grid, row - 1, column);
            const downCell: number = dfs(grid, row + 1, column);
            const leftCell: number = dfs(grid, row, column - 1);
            const rightCell: number = dfs(grid, row, column + 1);

            return upCell + downCell + leftCell + rightCell + 1;
        }
    }

    return 0;
}

function maxAreaOfIsland(grid: number[][]): number {
    let maxIslandCounter: number = 0;
    
    const rowSize: number = grid.length;
    const columnSize: number = grid[0].length;

    for (let row: number = 0; row < rowSize; row++)
        for (let column: number = 0; column < columnSize; column++)
            if (grid[row][column])
                maxIslandCounter = Math.max(maxIslandCounter, dfs(grid, row, column));

    return maxIslandCounter;
};
