/**
 * Checks if a given cell is valid within the grid.
 *
 * @param row - The row index of the cell.
 * @param column - The column index of the cell.
 * @param ROWS - The total number of rows in the grid.
 * @param COLUMNS - The total number of columns in the grid.
 * @returns `true` if the cell is valid, otherwise `false`.
 */
function isValidCell(row: number, column: number, ROWS: number, COLUMNS: number): boolean {
  const isValidRow: boolean = row >= 0 && row < ROWS;
  const isValidColumn: boolean = column >= 0 && column < COLUMNS;

  return isValidRow && isValidColumn;
}

/**
 * Finds the shortest path in a binary matrix from the top-left corner to the bottom-right corner.
 *
 * @param grid - The binary matrix representing the grid.
 * @returns The length of the shortest path from (0, 0) to (ROWS-1, COLUMNS-1), or -1 if no path exists.
 */
function shortestPathBinaryMatrix(grid: number[][]): number {
  const ROWS: number = grid.length;
  const COLUMNS: number = grid[0].length;

  const directions: number[][] = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1],
  ];

  const queue: number[][] = [[]];

  if (grid[0][0] === 0) {
    queue.push([0, 0, 1]);
    grid[0][0] = 1;
  }

  while (queue.length) {
    const currentLevel: number = queue.length;

    for (let level: number = 0; level < currentLevel; level++) {
      const [row, column, distance]: number[] = queue.shift()!;

      if (row === ROWS - 1 && column === COLUMNS - 1)
        return distance;

      for (const [rowOffset, columnOffset] of directions) {
        const nextRow: number = row + rowOffset;
        const nextColumn: number = column + columnOffset;

        if (
          isValidCell(nextRow, nextColumn, ROWS, COLUMNS) &&
          grid[nextRow][nextColumn] === 0
        ) {
          queue.push([nextRow, nextColumn, distance + 1]);
          grid[nextRow][nextColumn] = 1;
        }
      }
    }
  }

  return -1;
}
