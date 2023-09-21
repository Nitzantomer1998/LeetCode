/**
 * Checks if a given cell is a valid cell within the board.
 * @param board - The game board represented as a 2D array of strings.
 * @param row - The row index of the cell.
 * @param column - The column index of the cell.
 * @returns True if the cell is valid, otherwise false.
 */
function isValidCell(board: string[][], row: number, column: number): boolean {
  const ROWS: number = board.length;
  const COLUMNS: number = board[0].length;

  const isValidRow: boolean = row >= 0 && row < ROWS;
  const isValidColumn: boolean = column >= 0 && column < COLUMNS;

  return isValidRow && isValidColumn;
}

/**
 * Depth-first search (DFS) algorithm to recursively traverse and mark 'O' connected cells as 'U'.
 * @param board - The game board represented as a 2D array of strings.
 * @param row - The current row index.
 * @param column - The current column index.
 */
function dfs(board: string[][], row: number, column: number): void {
  if (isValidCell(board, row, column) == false) 
    return;

  if (board[row][column] !== "O")
    return;

  board[row][column] = "U";

  dfs(board, row - 1, column);
  dfs(board, row + 1, column);
  dfs(board, row, column - 1);
  dfs(board, row, column + 1);
}

/**
 * Solves the 'X' surrounded by 'O' problem on the game board.
 * @param board - The game board represented as a 2D array of strings.
 */
function solve(board: string[][]): void {
  const ROWS: number = board.length;
  const COLUMNS: number = board[0].length;

  for (let row: number = 0; row < ROWS; row++)
    for (let column: number = 0; column < COLUMNS; column++)
      if (row === 0 || row === ROWS - 1 || column === 0 || column === COLUMNS - 1)
        if (board[row][column] === "O") 
          dfs(board, row, column);

  for (let row: number = 0; row < ROWS; row++) {
    for (let column: number = 0; column < COLUMNS; column++) {
      if (board[row][column] === "O") 
        board[row][column] = "X";
      
      else if (board[row][column] === "U")
        board[row][column] = "O";
    }
  }
}
