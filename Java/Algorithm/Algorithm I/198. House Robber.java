class Solution {

  /**
   * Calculates the maximum amount that can be robbed from houses in a row
   * without robbing adjacent houses.
   *
   * @param nums An array representing the amount of money available in each house.
   * @return The maximum amount that can be robbed without robbing adjacent houses.
   */
  public int rob(int[] nums) {
    int NUMS_LENGTH = nums.length;

    for (int index = NUMS_LENGTH - 1; index >= 0; index--) {
      int firstOption = index + 2 < NUMS_LENGTH ? nums[index + 2] : 0;
      int secondOption = index + 3 < NUMS_LENGTH ? nums[index + 3] : 0;

      nums[index] += Math.max(firstOption, secondOption);
    }

    return NUMS_LENGTH > 1 ? Math.max(nums[0], nums[1]) : nums[0];
  }
}
