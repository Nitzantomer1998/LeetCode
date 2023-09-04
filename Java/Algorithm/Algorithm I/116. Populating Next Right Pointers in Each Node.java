class Solution {

  /**
   * Finds the single number in an array where every other element appears twice.
   *
   * @param nums An array of integers where all elements appear twice except one.
   * @return The unique number that appears only once.
   */
  public int singleNumber(int[] nums) {
    int NUMS_LENGTH = nums.length;

    int uniqueValue = 0;

    for (int index = 0; index < NUMS_LENGTH; index++) 
      uniqueValue = uniqueValue ^ nums[index];

    return uniqueValue;
  }
}
