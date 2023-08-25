function searchInsert(nums: number[], target: number): number {
    const numsLength: number = nums.length;

    let leftPointer: number = 0;
    let rightPointer: number = numsLength;

    while (leftPointer <= rightPointer) {
        const middlePointer: number = Math.floor((leftPointer + rightPointer) / 2);
        const middleValue: number = nums[middlePointer];

        if (middleValue === target)
            return middlePointer;

        else if (middleValue < target)
            leftPointer = middlePointer + 1;

        else
            rightPointer = middlePointer - 1;
    }

    return rightPointer + 1;
};
