/*
 * Finds the indices of two numbers in a sorted array that add up to a target value.
 *
 * The 'twoSum' function utilizes a two-pointer approach to find a pair of indices that
 * correspond to two numbers in the sorted input array, such that their sum matches the
 * given target value. It initializes two pointers, 'leftPointer' and 'rightPointer', at
 * the beginning and end of the array, respectively. The function calculates the sum of
 * the numbers pointed to by the two pointers and adjusts the pointers based on whether
 * the sum is greater or less than the target. This process continues until the sum equals
 * the target value, at which point the function returns the indices of the two numbers.
 *
 * Parameters:
 * - numbers: A pointer to a sorted array of integers.
 * - numbersSize: The number of elements in the array.
 * - target: The target sum to find.
 * - returnSize: A pointer to an integer that will store the size of the returned array.
 *
 * Returns:
 * A dynamically allocated integer array containing two indices whose corresponding
 * numbers add up to the target value. The caller is responsible for freeing the memory
 * allocated for the returned array.
 *
 * Note: The function assumes that there is exactly one solution, and the input array is
 * sorted in non-decreasing order.
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int *indicesSolution = malloc(2 * sizeof(int));
    
    int leftPointer = 0;
    int rightPointer = numbersSize - 1;
    int currentSum = numbers[leftPointer] + numbers[rightPointer];

    while (currentSum != target) {
        if (currentSum > target)
            rightPointer--;
        else
            leftPointer++;

        currentSum = numbers[leftPointer] + numbers[rightPointer];
    }

    indicesSolution[0] = leftPointer + 1;
    indicesSolution[1] = rightPointer + 1;
    *returnSize = 2;

    return indicesSolution;
}
