/**
 * Rotates a portion of an array between the start and end indices.
 * @param nums - The array of numbers to be rotated.
 * @param startIndex - The starting index of the rotation.
 * @param endIndex - The ending index of the rotation.
 */
function rotateArray(nums: number[], startIndex: number, endIndex: number): void {
  while (startIndex < endIndex) {
    const tempValue: number = nums[startIndex];

    nums[startIndex] = nums[endIndex];
    nums[endIndex] = tempValue;

    startIndex++;
    endIndex--;
  }
}

/**
 * Rotates the elements of an array to the right by a specified number of steps.
 * @param nums - The array of numbers to be rotated.
 * @param k - The number of steps to rotate the array.
 */
function rotate(nums: number[], k: number): void {
  const LENGTH: number = nums.length;

  k = k % LENGTH;

  rotateArray(nums, 0, LENGTH - 1);
  rotateArray(nums, 0, k - 1);
  rotateArray(nums, k, LENGTH - 1);
}
