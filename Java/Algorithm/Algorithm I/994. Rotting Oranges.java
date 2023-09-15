class Solution {

  /**
   * Determines the minimum number of minutes it takes for all oranges in a grid to rot.
   *
   * @param grid The grid representing the state of oranges (0 for empty, 1 for fresh, 2 for rotten).
   * @return The minimum number of minutes to make all oranges rotten, or -1 if not possible.
   */
  private boolean isValidCell(int[][] grid, int row, int column) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  public int orangesRotting(int[][] grid) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    int freshOrangeCounter = 0;
    int minutesCounter = 0;

    int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    Queue<int[]> rottenQueue = new LinkedList<>();

    for (int row = 0; row < ROWS; row++) {
      for (int column = 0; column < COLUMNS; column++) {
        if (grid[row][column] == 2) 
          rottenQueue.offer(new int[] { row, column }); 
        
        else if (grid[row][column] == 1) 
          freshOrangeCounter++;
      }
    }

    while (!rottenQueue.isEmpty()) {
      int currentLevelSize = rottenQueue.size();

      for (int i = 0; i < currentLevelSize; i++) {
        int[] currentOrange = rottenQueue.poll();

        for (int[] direction : directions) {
          int newRow = currentOrange[0] + direction[0];
          int newColumn = currentOrange[1] + direction[1];

          if (isValidCell(grid, newRow, newColumn)) {
            if (grid[newRow][newColumn] == 1) {
              grid[newRow][newColumn] = 2;
              rottenQueue.offer(new int[] { newRow, newColumn });
              freshOrangeCounter--;
            }
          }
        }
      }

      minutesCounter = rottenQueue.isEmpty() ? minutesCounter : minutesCounter + 1;
    }

    return freshOrangeCounter == 0 ? minutesCounter : -1;
  }
}
