class Solution {

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
