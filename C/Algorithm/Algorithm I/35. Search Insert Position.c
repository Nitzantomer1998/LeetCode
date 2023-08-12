/*
 * Searches for the position to insert a target value into a sorted integer array.
 *
 * The 'searchInsert' function searches for the position at which a given target value
 * should be inserted into a sorted integer array 'nums'. It employs a binary search
 * algorithm to efficiently locate the insertion point. The function initializes
 * 'leftPointer' to the beginning of the array and 'rightPointer' to the end of the array.
 * It then repeatedly calculates the middle index 'middlePointer' and compares the value
 * at that index with the target value. If the value at 'middlePointer' is equal to the
 * target value, the function immediately returns 'middlePointer'. If the value is greater
 * than the target, 'rightPointer' is adjusted to 'middlePointer - 1'. Otherwise,
 * 'leftPointer' is adjusted to 'middlePointer + 1'. The process continues until
 * 'leftPointer' is no longer less than or equal to 'rightPointer', at which point the
 * function returns 'rightPointer + 1', indicating the position where the target should
 * be inserted.
 *
 * Parameters:
 * - nums: A pointer to a sorted array of integers.
 * - numsSize: The number of elements in the array.
 * - target: The integer value to be inserted or located.
 *
 * Returns:
 * The index at which the target value should be inserted in the sorted array.
 *
 * This function efficiently determines the insertion position of the target value by using
 * binary search to find the appropriate index in the sorted array 'nums'.
 */
int searchInsert(int* nums, int numsSize, int target) {
    int leftPointer = 0;
    int rightPointer = numsSize - 1;

    while (leftPointer <= rightPointer) {
        int middlePointer = (leftPointer + rightPointer) / 2;
        int currentValue = nums[middlePointer];

        if (currentValue == target)
            return middlePointer;

        else if (currentValue > target)
            rightPointer = middlePointer - 1;

        else
            leftPointer = middlePointer + 1;
    }

    return rightPointer + 1;
}
