void merge(int* array, int leftPointer, int middlePointer, int rightPointer) {
    int leftSize = middlePointer - leftPointer + 1;
    int rightSize = rightPointer - middlePointer;

    int* leftArray = (int*) malloc (sizeof(int) * leftSize);
    int* rightArray = (int*) malloc (sizeof(int) * rightSize);

    for (int index = 0; index < leftSize; index++)
        leftArray[index] = array[leftPointer + index];
    
    for (int index = 0; index < rightSize; index++)
        rightArray[index] = array[middlePointer + 1 + index];

    int i = 0;
    int j = 0;
    int k = leftPointer;

    while (i < leftSize && j < rightSize) {
        if (leftArray[i] <= rightArray[j]) {
            array[k] = leftArray[i];
            i++;
        } 
        
        else {
            array[k] = rightArray[j];
            j++;
        }
        
        k++;
    }

    while (i < leftSize) {
        array[k] = leftArray[i];
        i++;
        k++;
    }

    while (j < rightSize) {
        array[k] = rightArray[j];
        j++;
        k++;
    }

    free(leftArray);
    free(rightArray);
}

void mergeSort(int* array, int leftPointer, int rightPointer) {
    if (leftPointer < rightPointer) {
        int middlePointer = (leftPointer + rightPointer) / 2;
        
        mergeSort(array, leftPointer, middlePointer);
        mergeSort(array, middlePointer + 1, rightPointer);
        
        merge(array, leftPointer, middlePointer, rightPointer);
    }
}

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* squareSortedArray = (int*) malloc (sizeof(int) * numsSize);
    *returnSize = numsSize;

    for (int index = 0; index < numsSize; index++) {
        int currentValue = nums[index];
        squareSortedArray[index] = currentValue * currentValue;
    }

    mergeSort(squareSortedArray, 0, numsSize - 1);
    
    return squareSortedArray;
}
