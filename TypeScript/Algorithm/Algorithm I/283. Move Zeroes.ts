function moveZeroes(nums: number[]): void {
    const numsLength: number = nums.length;
    let nonZeroIndex: number = 0;

    for (let index: number = 0; index < numsLength; index++) {
        if (nums[index]) {
            if (index !== nonZeroIndex) {
                nums[nonZeroIndex] = nums[index];
                nums[index] = 0;
            }
            nonZeroIndex++;
        }
    }
}
