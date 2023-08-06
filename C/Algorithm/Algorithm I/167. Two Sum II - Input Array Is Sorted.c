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
