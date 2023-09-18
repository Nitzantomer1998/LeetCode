import java.util.LinkedList;
import java.util.Queue;

class Solution {

  /**
   * Checks if a cell with given row and column indices is a valid cell within the grid.
   *
   * @param row     The row index of the cell.
   * @param column  The column index of the cell.
   * @param ROWS    The total number of rows in the grid.
   * @param COLUMNS The total number of columns in the grid.
   * @return True if the cell is valid, otherwise false.
   */
  private boolean isValidCell(int row, int column, int ROWS, int COLUMNS) {
    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  /**
   * Finds the shortest path in a binary matrix from the top-left corner (0, 0) to the
   * bottom-right corner (ROWS-1, COLUMNS-1).
   *
   * @param grid The binary matrix representing blocked (1) and unblocked (0) cells.
   * @return The length of the shortest path or -1 if no path exists.
   */
  public int shortestPathBinaryMatrix(int[][] grid) {
    int ROWS = grid.length;
    int COLUMNS = grid[0].length;

    int[][] directions = {
      { -1, 0 },
      { 1, 0 },
      { 0, -1 },
      { 0, 1 },
      { -1, -1 },
      { -1, 1 },
      { 1, -1 },
      { 1, 1 },
    };

    Queue<int[]> queue = new LinkedList<>();

    if (grid[0][0] == 0) {
      queue.offer(new int[] { 0, 0, 1 });
      grid[0][0] = 1;
    }

    while (!queue.isEmpty()) {
      int currentLevel = queue.size();

      for (int level = 0; level < currentLevel; level++) {
        int[] currentCell = queue.poll();

        int row = currentCell[0];
        int column = currentCell[1];
        int distance = currentCell[2];

        if (row == ROWS - 1 && column == COLUMNS - 1) return distance;

        for (int[] direction : directions) {
          int nextRow = row + direction[0];
          int nextColumn = column + direction[1];

          if (
            isValidCell(nextRow, nextColumn, ROWS, COLUMNS) &&
            grid[nextRow][nextColumn] == 0
          ) {
            queue.offer(new int[] { nextRow, nextColumn, distance + 1 });
            grid[nextRow][nextColumn] = 1;
          }
        }
      }
    }

    return -1;
  }
}
