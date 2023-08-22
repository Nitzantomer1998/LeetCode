/**
 * Rotates the elements of an array to the right by a specified number of steps.
 * @param nums - The array of numbers to be rotated.
 * @param k - The number of steps to rotate the array.
 */
function rotate(nums: number[], k: number): void {
    const numsLength: number = nums.length;
    
    k = k % numsLength;
    
    rotateArray(nums, 0, numsLength - 1);
    rotateArray(nums, 0, k - 1);
    rotateArray(nums, k, numsLength - 1);
}

/**
 * Rotates a portion of an array between the start and end indices.
 * @param nums - The array of numbers to be rotated.
 * @param start - The starting index of the rotation.
 * @param end - The ending index of the rotation.
 */
function rotateArray(nums: number[], start: number, end: number): void {
    while (start < end) {
        const temp: number = nums[start];

        nums[start] = nums[end];
        nums[end] = temp;
        
        start++;
        end--;
    }
}
