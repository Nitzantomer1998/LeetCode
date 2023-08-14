/**
 * Searches for a target value in a sorted array using binary search.
 *
 * The 'search' function performs a binary search on a sorted integer array 'nums'
 * to find the index of the target value. It compares the target value with the
 * middle element of the array and updates the search range accordingly until the
 * target is found or the search range is exhausted. If the target is found, the
 * index of the target value is returned; otherwise, -1 is returned.
 *
 * Parameters:
 * - nums: A sorted array of integers.
 * - numsSize: The number of elements in the array.
 * - target: The value to search for in the array.
 *
 * Returns:
 * The index of the target value in the array, or -1 if the target is not found.
 */
int search(int* nums, int numsSize, int target) {
    int leftPointer = 0;
    int rightPointer = numsSize - 1;

    while (leftPointer <= rightPointer) {
        int middlePointer = (leftPointer + rightPointer) / 2;
        int currentValue = nums[middlePointer];

        if (currentValue == target)
            return middlePointer;

        if (currentValue > target)
            rightPointer = middlePointer - 1;

        else
            leftPointer = middlePointer + 1;
    }

    return -1;
}
