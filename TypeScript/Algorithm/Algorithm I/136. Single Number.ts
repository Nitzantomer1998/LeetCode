/**
 * Finds the single number in an array where all other elements appear twice.
 * @param nums - An array of numbers where each element appears twice except for one element.
 * @returns The number that appears only once in the array.
 */
function singleNumber(nums: number[]): number {
  const LENGTH: number = nums.length;

  for (let index: number = LENGTH - 2; index >= 0; index--)
    nums[index] ^= nums[index + 1];

  return nums[0];
}
