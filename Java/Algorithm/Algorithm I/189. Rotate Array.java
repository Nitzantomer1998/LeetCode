class Solution {

  /**
   * Rotates a portion of an array in-place.
   *
   * @param nums       The array of integers to be rotated.
   * @param startIndex The starting index of the portion to rotate.
   * @param endIndex   The ending index of the portion to rotate.
   */
  private void arrayRotate(int[] nums, int startIndex, int endIndex) {
    while (startIndex < endIndex) {
      int tempValue = nums[startIndex];

      nums[startIndex] = nums[endIndex];
      nums[endIndex] = tempValue;

      startIndex++;
      endIndex--;
    }
  }

  /**
   * Rotates an array to the right by a specified number of steps.
   *
   * @param nums The array of integers to be rotated.
   * @param k    The number of steps to rotate the array to the right.
   */
  public void rotate(int[] nums, int k) {
    int NUMS_LENGTH = nums.length;

    k = k % NUMS_LENGTH;

    this.arrayRotate(nums, 0, NUMS_LENGTH - 1);
    this.arrayRotate(nums, k, NUMS_LENGTH - 1);
    this.arrayRotate(nums, 0, k - 1);
  }
}
