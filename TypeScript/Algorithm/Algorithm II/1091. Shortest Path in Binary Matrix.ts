function isValidCell(row: number, column: number, ROWS: number, COLUMNS: number): boolean {
  const isValidRow: boolean = row >= 0 && row < ROWS;
  const isValidColumn: boolean = column >= 0 && column < COLUMNS;

  return isValidRow && isValidColumn;
}

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
