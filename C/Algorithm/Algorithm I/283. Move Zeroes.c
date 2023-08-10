/*
 * Moves all zeros in an array to the end while maintaining the relative order of other elements.
 *
 * The 'moveZeroes' function rearranges the elements of an integer array 'nums' to move all
 * occurrences of zeros to the end of the array, while keeping the relative order of the
 * non-zero elements unchanged. It does so by iterating through the array and using a
 * 'zeroIndex' to keep track of the position where non-zero elements should be placed. For
 * each non-zero element, it swaps the current element with the element at 'zeroIndex' and
 * increments 'zeroIndex'. After processing all elements, it fills the remaining positions
 * with zeros to ensure all zeros are moved to the end of the array.
 *
 * Parameters:
 * - nums: A pointer to an array of integers.
 * - numsSize: The number of elements in the array.
 *
 * This function modifies the input 'nums' array in place to move all zeros to the end while
 * maintaining the relative order of other elements.
 */
void moveZeroes(int* nums, int numsSize) {
    int zeroIndex = 0;

    for (int index = 0; index < numsSize; index++)
        if (nums[index] != 0)
            nums[zeroIndex++] = nums[index];
    
    while (zeroIndex < numsSize)
        nums[zeroIndex++] = 0;
}
