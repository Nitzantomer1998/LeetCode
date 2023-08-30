function search(nums: number[], target: number): number {
    const numsLength: number = nums.length;
    
    let leftPointer: number = 0;
    let rightPointer: number = numsLength - 1;

    while (leftPointer <= rightPointer) {
        const middlePointer: number = Math.floor((leftPointer + rightPointer) / 2);
        const middleValue: number = nums[middlePointer];

        if (middleValue === target)
            return middlePointer;

        else if (middleValue > target)
            rightPointer = middlePointer - 1;

        else
            leftPointer = middlePointer + 1;
    }

    return -1;
};
