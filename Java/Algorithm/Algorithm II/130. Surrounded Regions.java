class Solution {

  private boolean isValidCell(char[][] board, int row, int column) {
    int ROWS = board.length;
    int COLUMNS = board[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  private void dfs(char[][] board, int row, int column) {
    if (this.isValidCell(board, row, column) == false) 
        return;

    if (board[row][column] != 'O')
        return;
    
    board[row][column] = 'U';

    this.dfs(board, row - 1, column);
    this.dfs(board, row + 1, column);
    this.dfs(board, row, column - 1);
    this.dfs(board, row, column + 1);
  }

  public void solve(char[][] board) {
    int ROWS = board.length;
    int COLUMNS = board[0].length;

    for (int row = 0; row < ROWS; row++) 
      for (int column = 0; column < COLUMNS; column++) 
        if (row == 0 || row == ROWS - 1 || column == 0 || column == COLUMNS - 1) 
          if (board[row][column] == 'O') 
            this.dfs(board, row, column);

    for (int row = 0; row < ROWS; row++) {
      for (int column = 0; column < COLUMNS; column++) {
        if (board[row][column] == 'O') 
          board[row][column] = 'X'; 
          
        else if (board[row][column] == 'U') 
          board[row][column] = 'O';
      }
    }
  }
}
