void swapValues(int* valueA, int* valueB) {
    int temp = *valueA;

    *valueA = *valueB;
    *valueB = temp;
}

void rotateArray(int* start, int* end) {
    while (start < end)
        swapValues(start++, --end);
}

void rotate(int* nums, int numsSize, int k) {
    k = numsSize - k % numsSize;
    
    rotateArray(nums, nums + k);
    rotateArray(nums + k, nums + numsSize);
    rotateArray(nums, nums + numsSize);
}
