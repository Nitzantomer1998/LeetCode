class Solution {

  /**
   * Moves all zeroes to the end of an integer array while maintaining the relative order of non-zero elements.
   *
   * @param nums An array of integers containing zeroes and non-zeroes.
   */
  public void moveZeroes(int[] nums) {
    int NUMS_LENGTH = nums.length;
    int nonZeroIndex = 0;

    for (int index = 0; index < NUMS_LENGTH; index++) {
      if (nums[index] != 0) {
        int tempValue = nums[index];

        nums[index] = nums[nonZeroIndex];
        nums[nonZeroIndex] = tempValue;

        nonZeroIndex++;
      }
    }
  }
}
