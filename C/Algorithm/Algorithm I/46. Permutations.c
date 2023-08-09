void swapValues(int *valueA, int *valueB) {
    int temp = *valueA;

    *valueA = *valueB;
    *valueB = temp;
}

void dfs(int* nums, int numsSize, int*** permuted, int* returnSize,  int** returnColumnSizes, int curr) {
    
    if (curr >= numsSize - 1) {
        *returnSize += 1;
        (*returnColumnSizes)[*returnSize - 1] = numsSize;
        (*permuted)[*returnSize - 1] = (int*) malloc (sizeof(int) * numsSize);
        
        for (int index = 0; index < numsSize; index++) 
            (*permuted)[*returnSize - 1][index] = nums[index]; 
        
        return;
    }
    
    for (int index = curr; index < numsSize; index++) {
        swapValues(nums + curr, nums + index);
        dfs(nums, numsSize, permuted, returnSize, returnColumnSizes, curr + 1);
        swapValues(nums + curr, nums + index);
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {     
    *returnSize = 1;
    for (int i = 1; i <= numsSize; ++i)
        (*returnSize) *= i; 

    int **permutatedArray = (int**) malloc (sizeof(int*) * *returnSize);
    *returnColumnSizes = (int*) malloc (sizeof(int) * *returnSize);
    
    *returnSize = 0;
    dfs(nums, numsSize, &permutatedArray, returnSize, returnColumnSizes, 0);
    
    return permutatedArray;
}
