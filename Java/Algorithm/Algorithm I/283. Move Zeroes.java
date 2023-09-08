class Solution {

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
