/*
 * Swaps the values of two integer variables.
 *
 * The 'swapValues' function takes two pointers to integer variables as parameters and
 * swaps their values using a temporary variable. This function provides a simple way to
 * exchange values between two variables.
 *
 * Parameters:
 * - valueA: A pointer to the first integer variable.
 * - valueB: A pointer to the second integer variable.
 *
 * This function modifies the values of 'valueA' and 'valueB' in place, effectively
 * swapping their contents.
 */
void swapValues(int* valueA, int* valueB) {
    int temp = *valueA;

    *valueA = *valueB;
    *valueB = temp;
}

/*
 * Rotates an array of integers by a given number of steps.
 *
 * The 'rotateArray' function rotates the elements of an array in place by reversing the
 * order of elements within a specified range. It takes two pointers, 'start' and 'end',
 * which represent the range of elements to be rotated. The function repeatedly swaps
 * elements from the start and end of the range towards the center until the entire range
 * is reversed.
 *
 * Parameters:
 * - start: A pointer to the first element of the range.
 * - end: A pointer to the element after the last element of the range.
 *
 * This function modifies the input array in place, effectively rotating the elements
 * within the specified range.
 */
void rotateArray(int* start, int* end) {
    while (start < end)
        swapValues(start++, --end);
}

/*
 * Rotates an array of integers to the right by a given number of steps.
 *
 * The 'rotate' function performs a right rotation on the input array 'nums' by 'k' steps.
 * It first calculates the effective rotation amount by adjusting 'k' to ensure it is
 * within the array's bounds. Then, it uses the 'rotateArray' function to perform three
 * separate reversals: first, for the elements up to 'k'; second, for the elements from
 * 'k' to the end of the array; and third, for the entire array. This effectively
 * achieves the desired rotation.
 *
 * Parameters:
 * - nums: A pointer to an array of integers.
 * - numsSize: The number of elements in the array.
 * - k: The number of steps to rotate the array to the right.
 *
 * This function modifies the input 'nums' array in place, performing a right rotation by
 * 'k' steps.
 */
void rotate(int* nums, int numsSize, int k) {
    k = numsSize - k % numsSize;
    
    rotateArray(nums, nums + k);
    rotateArray(nums + k, nums + numsSize);
    rotateArray(nums, nums + numsSize);
}
