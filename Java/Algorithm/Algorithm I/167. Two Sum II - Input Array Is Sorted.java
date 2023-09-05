class Solution {

  /**
   * Finds two numbers in a sorted array that add up to a given target sum.
   *
   * @param numbers An array of integers sorted in ascending order.
   * @param target  The target sum to find.
   * @return An array containing the indices (1-based) of the two numbers that add up to the target sum.
   */
  public int[] twoSum(int[] numbers, int target) {
    int NUMBERS_LENGTH = numbers.length;

    int leftPointer = 0;
    int rightPointer = NUMBERS_LENGTH - 1;

    while (leftPointer < rightPointer) {
      int sumValue = numbers[leftPointer] + numbers[rightPointer];

      if (sumValue == target) break;
      else if (sumValue > target) rightPointer--; 
      else leftPointer++;
    }

    return new int[] { leftPointer + 1, rightPointer + 1 };
  }
}
