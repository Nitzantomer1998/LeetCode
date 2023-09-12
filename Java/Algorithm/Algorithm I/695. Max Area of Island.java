class Solution {

  /**
   * Checks if a cell is a valid cell within the given grid.
   *
   * @param grid   The grid to check cell validity within.
   * @param row    The row index of the cell.
   * @param column The column index of the cell.
   * @return True if the cell is valid, otherwise false.
   */
  private boolean isValidCell(int grid[][], int row, int column) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  /**
   * Performs depth-first search (DFS) to calculate the area of an island.
   *
   * @param grid   The grid representing the landmass.
   * @param row    The current row index.
   * @param column The current column index.
   * @return The area of the island starting from the given cell.
   */
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

  /**
   * Finds the maximum area of an island in the given grid.
   *
   * @param grid The grid representing the landmass where 1's indicate land and 0's indicate water.
   * @return The maximum area of an island.
   */
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
