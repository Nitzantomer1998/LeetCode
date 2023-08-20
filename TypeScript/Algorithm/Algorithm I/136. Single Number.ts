function singleNumber(nums: number[]): number {
    const numsLength: number = nums.length;

    for (let index: number = numsLength - 2; index >= 0; index--)
        nums[index] ^= nums[index + 1];

    return nums[0];
}
