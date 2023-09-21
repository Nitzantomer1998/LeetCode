function isValidCell(board: string[][], row: number, column: number): boolean {
  const ROWS: number = board.length;
  const COLUMNS: number = board[0].length;

  const isValidRow: boolean = row >= 0 && row < ROWS;
  const isValidColumn: boolean = column >= 0 && column < COLUMNS;

  return isValidRow && isValidColumn;
}

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
