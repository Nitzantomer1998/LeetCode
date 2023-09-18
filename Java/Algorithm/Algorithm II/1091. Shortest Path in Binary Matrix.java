import java.util.LinkedList;
import java.util.Queue;

class Solution {

  private boolean isValidCell(int row, int column, int ROWS, int COLUMNS) {
    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

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
