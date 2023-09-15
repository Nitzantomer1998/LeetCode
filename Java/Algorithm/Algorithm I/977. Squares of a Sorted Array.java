class Solution {

  public int[] sortedSquares(int[] nums) {
    int NUMS_LENGTH = nums.length;

    int[] sortedSquareArray = new int[NUMS_LENGTH];
    int indexInsertion = NUMS_LENGTH - 1;

    int leftPointer = 0;
    int rightPointer = NUMS_LENGTH - 1;

    while (leftPointer <= rightPointer) {
      int firstValue = Math.abs(nums[leftPointer]);
      int lastValue = Math.abs(nums[rightPointer]);

      if (firstValue > lastValue) {
        sortedSquareArray[indexInsertion] = firstValue * firstValue;
        leftPointer++;
      } 
      
      else {
        sortedSquareArray[indexInsertion] = lastValue * lastValue;
        rightPointer--;
      }

      indexInsertion--;
    }

    return sortedSquareArray;
  }
}
