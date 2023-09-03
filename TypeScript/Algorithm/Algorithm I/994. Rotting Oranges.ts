/**
 * Determines the time needed for all oranges in the grid to become rotten.
 * @param {number[][]} grid - The grid representing the orange matrix.
 * @returns {number} The time required for all oranges to become rotten, or -1 if not possible.
 */
function orangesRotting(grid: number[][]): number {
  const FRESH: number = 1;
  const ROTTEN: number = 2;

  const ROWS: number = grid.length;
  const COLUMNS: number = grid[0].length;

  let rottenOrangeQueue: { row: number; column: number }[] = [];
  let freshOrangeCounter: number = 0;
  let rottenOrangeTimer: number = 0;

  let directions = [
    { row: 1, column: 0 }, // Down
    { row: -1, column: 0 }, // Up
    { row: 0, column: 1 }, // Right
    { row: 0, column: -1 }, // Left
  ];

  for (let row: number = 0; row < ROWS; row++) {
    for (let column: number = 0; column < COLUMNS; column++) {
      if (grid[row][column] === FRESH) 
        freshOrangeCounter++;
      
      else if (grid[row][column] === ROTTEN)
        rottenOrangeQueue.push({ row, column });
    }
  }

  while (freshOrangeCounter > 0 && rottenOrangeQueue.length > 0) {
    const QUEUE_LENGTH: number = rottenOrangeQueue.length;

    for (let i: number = 0; i < QUEUE_LENGTH; i++) {
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
