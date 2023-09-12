class Solution {

  private boolean isValidCell(int grid[][], int row, int column) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  private int dfs(int[][] grid, int row, int column) {
    if (isValidCell(grid, row, column)) {
      if (grid[row][column] != 0) {
        grid[row][column] = 0;

        int upCell = dfs(grid, row - 1, column);
        int downCell = dfs(grid, row + 1, column);
        int leftCell = dfs(grid, row, column - 1);
        int rightCell = dfs(grid, row, column + 1);

        return upCell + downCell + leftCell + rightCell + 1;
      }
    }

    return 0;
  }

  public int maxAreaOfIsland(int[][] grid) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    int maxIslandArea = 0;

    for (int row = 0; row < ROWS; row++) 
      for (int column = 0; column < COLUMNS; column++) 
        if (grid[row][column] != 0) 
          maxIslandArea = Math.max(maxIslandArea, dfs(grid, row, column));

    return maxIslandArea;
  }
}
