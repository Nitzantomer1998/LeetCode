void moveZeroes(int* nums, int numsSize) {
    int zeroIndex = 0;

    for (int index = 0; index < numsSize; index++)
        if (nums[index] != 0)
            nums[zeroIndex++] = nums[index];
    
    while (zeroIndex < numsSize)
        nums[zeroIndex++] = 0;
}
