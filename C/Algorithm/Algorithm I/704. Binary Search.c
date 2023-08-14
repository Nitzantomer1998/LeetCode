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
