/**
 * Finds all unique triplets in the given array of numbers that sum up to zero.
 * @param nums - An array of numbers.
 * @returns An array of unique triplets that sum up to zero.
 */
function threeSum(nums: number[]): number[][] {
  const NUMS_LENGTH: number = nums.length;

  const uniqueSolution: number[][] = [];

  nums.sort((a, b) => a - b);

  for (let i: number = 0; i < NUMS_LENGTH; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) 
      continue;

    let left: number = i + 1;
    let right: number = NUMS_LENGTH - 1;

    while (left < right) {
      const currentSum: number = nums[i] + nums[left] + nums[right];

      if (currentSum > 0) 
        right--;
      
      else if (currentSum < 0) 
        left++;
      
      else {
        uniqueSolution.push([nums[i], nums[left], nums[right]]);
        left++;

        while (left < right && nums[left] === nums[left - 1]) 
          left++;
      }
    }
  }

  return uniqueSolution;
}
