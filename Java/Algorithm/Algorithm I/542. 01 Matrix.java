class Solution {

  /**
   * Checks if a cell is a valid cell within the given matrix.
   *
   * @param mat    The matrix to check cell validity within.
   * @param row    The row index of the cell.
   * @param column The column index of the cell.
   * @return True if the cell is valid, otherwise false.
   */
  private boolean isValidCell(int[][] mat, int row, int column) {
    int ROWS = mat.length;
    int COLUMNS = mat[0].length;

    boolean isRowValid = row >= 0 && row < ROWS;
    boolean isColumnValid = column >= 0 && column < COLUMNS;

    return isRowValid && isColumnValid;
  }

  /**
   * Computes the minimum distance from 1-valued cells to 0-valued cells in a binary matrix.
   *
   * @param mat The binary matrix where 0 represents empty cells and 1 represents obstacles.
   * @return A matrix representing the minimum distance from each 1-valued cell to the nearest 0-valued cell.
   */
  public int[][] updateMatrix(int[][] mat) {
    int ROWS = mat.length;
    int COLUMNS = mat[0].length;

    int[][] distanceMat = new int[ROWS][COLUMNS];
    Queue<int[]> queue = new LinkedList<>();

    for (int row = 0; row < ROWS; row++) {
      for (int column = 0; column < COLUMNS; column++) {
        if (mat[row][column] == 0) {
          queue.offer(new int[] { row, column });
          distanceMat[row][column] = 0;
        } 
        
        else {
          distanceMat[row][column] = Integer.MAX_VALUE;
        }
      }
    }

    int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    while (!queue.isEmpty()) {
      int[] currentCell = queue.poll();
      int row = currentCell[0];
      int column = currentCell[1];

      for (int[] direction : directions) {
        int newRow = row + direction[0];
        int newColumn = column + direction[1];

        if (isValidCell(mat, newRow, newColumn)) {
          if (distanceMat[newRow][newColumn] > distanceMat[row][column] + 1) {
            distanceMat[newRow][newColumn] = distanceMat[row][column] + 1;
            queue.offer(new int[] { newRow, newColumn });
          }
        }
      }
    }

    return distanceMat;
  }
}
