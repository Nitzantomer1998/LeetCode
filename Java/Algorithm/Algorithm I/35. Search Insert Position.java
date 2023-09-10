class Solution {

  public int searchInsert(int[] nums, int target) {
    int NUMS_LENGTH = nums.length;

    int leftPointer = 0;
    int rightPointer = NUMS_LENGTH - 1;

    while (leftPointer <= rightPointer) {
      int middlePointer = leftPointer + (rightPointer - leftPointer) / 2;
      int middleValue = nums[middlePointer];

      if (middleValue == target) 
        return middlePointer;
      
      else if (middleValue > target) 
        rightPointer = middlePointer - 1;
      
      else 
        leftPointer = middlePointer + 1;
    }

    return rightPointer + 1;
  }
}
