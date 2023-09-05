class Solution {

  private void arrayRotate(int[] nums, int startIndex, int endIndex) {
    while (startIndex < endIndex) {
      int tempValue = nums[startIndex];

      nums[startIndex] = nums[endIndex];
      nums[endIndex] = tempValue;

      startIndex++;
      endIndex--;
    }
  }

  public void rotate(int[] nums, int k) {
    int NUMS_LENGTH = nums.length;

    k = k % NUMS_LENGTH;

    this.arrayRotate(nums, 0, NUMS_LENGTH - 1);
    this.arrayRotate(nums, k, NUMS_LENGTH - 1);
    this.arrayRotate(nums, 0, k - 1);
  }
}
