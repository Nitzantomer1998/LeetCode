class Solution {

  /**
   * Searches for the target element in a sorted array using binary search.
   *
   * @param nums   The sorted array to search in.
   * @param target The target element to find.
   * @return The index of the target element if found, otherwise -1.
   */
  public int search(int[] nums, int target) {
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

    return -1;
  }
}
