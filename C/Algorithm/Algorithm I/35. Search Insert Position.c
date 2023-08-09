int searchInsert(int* nums, int numsSize, int target) {
    int leftPointer = 0;
    int rightPointer = numsSize - 1;

    while (leftPointer <= rightPointer) {
        int middlePointer = (leftPointer + rightPointer) / 2;

        if (nums[middlePointer] == target)
            return middlePointer;

        else if (nums[middlePointer] > target)
            rightPointer = middlePointer - 1;

        else
            leftPointer = middlePointer + 1;
    }

    return rightPointer + 1;
}
