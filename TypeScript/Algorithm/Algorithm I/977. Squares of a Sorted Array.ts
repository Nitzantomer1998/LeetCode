/**
 * Squares each element of a sorted array and returns a new array sorted in non-decreasing order.
 * @param {number[]} nums - The sorted array of integers.
 * @returns {number[]} A new sorted array with each element squared.
 */
function sortedSquares(nums: number[]): number[] {
  const numsLength: number = nums.length;
  const squareSortArray: number[] = new Array(numsLength);

  let leftPointer: number = 0;
  let rightPointer: number = numsLength - 1;

  for (let index: number = numsLength - 1; index >= 0; index--) {
    const squareStart: number = nums[leftPointer] ** 2;
    const squareEnd: number = nums[rightPointer] ** 2;

    squareSortArray[index] = squareEnd > squareStart ? squareEnd : squareStart;

    if (squareEnd > squareStart) rightPointer--;
    else leftPointer++;
  }

  return squareSortArray;
}
