/*
 * Finds the single number in an array where every element appears twice except for one.
 *
 * The 'singleNumber' function employs the XOR (^) bitwise operation to find the unique
 * element that appears only once in the array. It iterates through the array in reverse
 * order, bitwise XOR-ing each element with the subsequent element. The final result will
 * be the unique element.
 *
 * Parameters:
 * - nums: A pointer to an array of integers.
 * - numsSize: The number of elements in the array.
 *
 * Returns:
 * The unique element that appears only once in the array.
 *
 * This function modifies the input 'nums' array in place by applying bitwise XOR to
 * adjacent elements, effectively canceling out the elements that appear twice. The
 * remaining element will be the one that appears only once.
 */
int singleNumber(int* nums, int numsSize) {
   for (int index = numsSize - 2; index > -1; index--)
        nums[index] ^= nums[index + 1];

    return nums[0];
}
