class Solution {

  /**
   * Searches for the target element in a sorted array and returns its index if found.
   * If the target is not found, returns the index where it would be inserted while maintaining the sorted order.
   *
   * @param nums   The sorted array of integers to search in.
   * @param target The target element to search for.
   * @return The index of the target element if found, or the index to insert it if not found.
   */
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
