/**
 * Searches for the position to insert a target value in a sorted array.
 * @param {number[]} nums - The sorted array of numbers.
 * @param {number} target - The target value to be inserted.
 * @returns {number} The index where the target value should be inserted.
 */
function searchInsert(nums: number[], target: number): number {
  const LENGTH: number = nums.length;

  let leftPointer: number = 0;
  let rightPointer: number = LENGTH;

  while (leftPointer <= rightPointer) {
    const middlePointer: number = Math.floor((leftPointer + rightPointer) / 2);
    const middleValue: number = nums[middlePointer];

    if (middleValue === target) return middlePointer;
    else if (middleValue < target) leftPointer = middlePointer + 1;
    else rightPointer = middlePointer - 1;
  }

  return rightPointer + 1;
}
