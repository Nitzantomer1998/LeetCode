class Solution {

  public int singleNumber(int[] nums) {
    int NUMS_LENGTH = nums.length;

    int uniqueValue = 0;

    for (int index = 0; index < NUMS_LENGTH; index++) 
      uniqueValue = uniqueValue ^ nums[index];

    return uniqueValue;
  }
}
