class Solution {

  private boolean isValidCell(int[][] image, int row, int column) {
    int ROWS = image.length;
    int COLUMNS = image[0].length;

    boolean isValidRow = row >= 0 && row < ROWS;
    boolean isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
  }

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
