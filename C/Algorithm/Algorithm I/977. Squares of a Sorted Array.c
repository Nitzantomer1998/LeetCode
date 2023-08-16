/**
 * Merges two subarrays of the input array in sorted order.
 *
 * The 'merge' function takes an input array, and two indices 'leftPointer' and 'rightPointer'
 * that define the subarrays to be merged. It creates temporary arrays for the left and right
 * subarrays, then merges them back into the input array in sorted order.
 *
 * Parameters:
 * - array: The input array containing two subarrays to be merged.
 * - leftPointer: The index of the start of the left subarray.
 * - middlePointer: The index of the end of the left subarray and the start of the right subarray.
 * - rightPointer: The index of the end of the right subarray.
 */
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

/**
 * Applies the merge sort algorithm to sort an input array.
 *
 * The 'mergeSort' function implements the merge sort algorithm to sort the elements of an input array.
 * It recursively divides the array into subarrays, sorts each subarray, and then merges them together.
 *
 * Parameters:
 * - array: The input array to be sorted.
 * - leftPointer: The index of the start of the subarray to be sorted.
 * - rightPointer: The index of the end of the subarray to be sorted.
 */
void mergeSort(int* array, int leftPointer, int rightPointer) {
    if (leftPointer < rightPointer) {
        int middlePointer = (leftPointer + rightPointer) / 2;
        
        mergeSort(array, leftPointer, middlePointer);
        mergeSort(array, middlePointer + 1, rightPointer);
        
        merge(array, leftPointer, middlePointer, rightPointer);
    }
}

/**
 * Generates an array of sorted squares from the input array of integers.
 *
 * The 'sortedSquares' function takes an array of integers 'nums', squares each element, and then
 * applies the merge sort algorithm to sort the squared values in ascending order. The sorted
 * squared values are returned in a new dynamically allocated array.
 *
 * Parameters:
 * - nums: The input array of integers.
 * - numsSize: The size of the input array.
 * - returnSize: A pointer to the variable that will store the size of the sorted array.
 *
 * Returns:
 * A dynamically allocated array of integers representing the sorted squares of the input array.
 */
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
