/**
 * Finds a pair of numbers in a sorted array that add up to the given target.
 * @param numbers - A sorted array of numbers.
 * @param target - The target sum to be achieved.
 * @returns An array containing the indices of the two numbers that add up to the target.
 */
function twoSum(numbers: number[], target: number): number[] {
    const numbersLength: number = numbers.length;

    let leftPointer: number = 0;
    let rightPointer: number = numbersLength - 1;

    while (leftPointer < rightPointer) {
        const currentSum: number = numbers[leftPointer] + numbers[rightPointer];

        if (currentSum === target)
            return [leftPointer + 1, rightPointer + 1];

        else if (currentSum > target)
            rightPointer--;
    
        else
            leftPointer++;
    }

    return [leftPointer + 1, rightPointer + 1];
};
