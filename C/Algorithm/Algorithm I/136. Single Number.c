int singleNumber(int* nums, int numsSize) {
   for (int index = numsSize - 2; index > -1; index--)
        nums[index] ^= nums[index + 1];

    return nums[0];
}
