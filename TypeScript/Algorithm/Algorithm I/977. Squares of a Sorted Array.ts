function orangesRotting(grid: number[][]): number {
  const FRESH: number = 1;
  const ROTTEN: number = 2;

  const ROWS: number = grid.length;
  const COLUMNS: number = grid[0].length;

  let rottenOrangeQueue: { row: number; column: number }[] = [];
  let freshOrangeCounter: number = 0;
  let rottenOrangeTimer: number = 0;

  let directions = [
    { row: 1, column: 0 },
    { row: -1, column: 0 },
    { row: 0, column: 1 },
    { row: 0, column: -1 },
  ];

  for (let row: number = 0; row < ROWS; row++) {
    for (let column: number = 0; column < COLUMNS; column++) {
      if (grid[row][column] === FRESH) freshOrangeCounter++;
      else if (grid[row][column] === ROTTEN) rottenOrangeQueue.push({ row, column });
    }
  }

  while (freshOrangeCounter > 0 && rottenOrangeQueue.length > 0) {
    let queueLength: number = rottenOrangeQueue.length;

    for (let i: number = 0; i < queueLength; i++) {
      let { row, column } = rottenOrangeQueue.shift()!;

      for (let direction of directions) {
        let newRow: number = row + direction.row;
        let newColumn: number = column + direction.column;

        if (newRow >= 0 && newColumn >= 0 && newRow < ROWS && newColumn < COLUMNS) {
          if (grid[newRow][newColumn] === FRESH) {
            rottenOrangeQueue.push({ row: newRow, column: newColumn });
            grid[newRow][newColumn] = ROTTEN;
            freshOrangeCounter--;
          }
        }
      }
    }
    rottenOrangeTimer++;
  }

  return freshOrangeCounter === 0 ? rottenOrangeTimer : -1;
}
