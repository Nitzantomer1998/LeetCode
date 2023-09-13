class Solution {

  /**
   * Checks if a cell is a valid cell within the given image.
   *
   * @param image  The image grid to check cell validity within.
   * @param row    The row index of the cell.
   * @param column The column index of the cell.
   * @return True if the cell is valid, otherwise false.
   */
  private boolean isValidCell(int[][] image, int row, int column) {
    int ROWS = image.length;
    int COLUMNS = image[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

  /**
   * Performs depth-first search (DFS) to fill an area of the image with a new color.
   *
   * @param image    The image grid to be filled.
   * @param row      The current row index.
   * @param column   The current column index.
   * @param oldColor The original color to be replaced.
   * @param newColor The new color to fill the area with.
   */
  private void dfs(int[][] image, int row, int column, int oldColor, int newColor) {
    if (isValidCell(image, row, column)) {
      if (image[row][column] == oldColor) {
        image[row][column] = newColor;

        dfs(image, row - 1, column, oldColor, newColor);
        dfs(image, row + 1, column, oldColor, newColor);
        dfs(image, row, column - 1, oldColor, newColor);
        dfs(image, row, column + 1, oldColor, newColor);
      }
    }
  }

  /**
   * Fills the area of the image starting from a specified cell with a new color.
   *
   * @param image The image grid to be filled.
   * @param sr    The row index of the starting cell.
   * @param sc    The column index of the starting cell.
   * @param color The new color to fill the area with.
   * @return The modified image with the filled area.
   */
  public int[][] floodFill(int[][] image, int sr, int sc, int color) {
    int ROWS = image.length;
    int COLUMNS = image[0].length;

    int newColor = color;
    int oldColor = image[sr][sc];

    if (oldColor == newColor) return image;

    dfs(image, sr, sc, oldColor, newColor);

    return image;
  }
}
