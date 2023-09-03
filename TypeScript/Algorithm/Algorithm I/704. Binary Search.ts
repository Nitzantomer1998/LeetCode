/**
 * Searches for a target value in a sorted array using binary search.
 * @param {number[]} nums - The sorted array to search in.
 * @param {number} target - The target value to search for.
 * @returns {number} The index of the target value in the array, or -1 if not found.
 */
function search(nums: number[], target: number): number {
  const LENGTH: number = nums.length;

  let leftPointer: number = 0;
  let rightPointer: number = LENGTH - 1;

  while (leftPointer <= rightPointer) {
    const middlePointer: number = Math.floor((leftPointer + rightPointer) / 2);
    const middleValue: number = nums[middlePointer];

    if (middleValue === target) return middlePointer;
    else if (middleValue > target) rightPointer = middlePointer - 1;
    else leftPointer = middlePointer + 1;
  }

  return -1;
}
