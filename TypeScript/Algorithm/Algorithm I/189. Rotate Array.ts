function rotate(nums: number[], k: number): void {
    const numsLength: number = nums.length;
    
    k = k % numsLength;
    
    rotateArray(nums, 0, numsLength - 1);
    rotateArray(nums, 0, k - 1);
    rotateArray(nums, k, numsLength - 1);
}

function rotateArray(nums: number[], start: number, end: number): void {
    while (start < end) {
        const temp: number = nums[start];

        nums[start] = nums[end];
        nums[end] = temp;
        
        start++;
        end--;
    }
}
