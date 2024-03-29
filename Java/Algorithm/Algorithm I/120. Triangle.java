import java.util.List;

class Solution {

  /**
   * Calculates the minimum path sum from the top to the bottom of a triangle.
   *
   * @param triangle A List of Lists representing the triangle with integer values.
   * @return The minimum path sum.
   */
  public int minimumTotal(List<List<Integer>> triangle) {
    int ROWS = triangle.size();

    for (int row = ROWS - 2; row >= 0; row--) {
      int COLUMNS = triangle.get(row).size();

      for (int column = 0; column < COLUMNS; column++) {
        int currentCellValue = triangle.get(row).get(column);
        int nextRowValue1 = triangle.get(row + 1).get(column);
        int nextRowValue2 = triangle.get(row + 1).get(column + 1);

        triangle
          .get(row)
          .set(
            column,
            currentCellValue + Math.min(nextRowValue1, nextRowValue2)
          );
      }
    }

    return triangle.get(0).get(0);
  }
}
