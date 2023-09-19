class Solution {

  /**
   * Finds the maximum area that can be formed by two vertical lines and the x-axis
   * with the bars represented by the given array.
   *
   * @param height An array of bar heights.
   * @return The maximum area formed by two vertical lines and the x-axis.
   */
  public int maxArea(int[] height) {
    int HEIGHT_LENGTH = height.length;

    int maxContainer = 0;

    int leftPointer = 0;
    int rightPointer = HEIGHT_LENGTH - 1;

    while (leftPointer < rightPointer) {
      int leftBar = height[leftPointer];
      int rightBar = height[rightPointer];
      int barDistance = rightPointer - leftPointer;

      int currentContainer = Math.min(leftBar, rightBar) * barDistance;
      maxContainer = Math.max(maxContainer, currentContainer);

      if (leftBar < rightBar) leftPointer++;
      else rightPointer--;
    }

    return maxContainer;
  }
}
