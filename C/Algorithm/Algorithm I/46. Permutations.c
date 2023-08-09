/*
 * Swaps the values of two integers.
 *
 * The 'swapValues' function takes two pointers to integers 'valueA' and 'valueB' as input
 * and swaps their values. It uses a temporary variable 'temp' to store the value of
 * 'valueA', then assigns the value of 'valueB' to 'valueA' and finally assigns the stored
 * value of 'valueA' to 'valueB'. After the function is executed, the values of 'valueA'
 * and 'valueB' are effectively swapped.
 *
 * Parameters:
 * - valueA: A pointer to the first integer to be swapped.
 * - valueB: A pointer to the second integer to be swapped.
 *
 * This function performs an in-place swap of two integer values, effectively swapping
 * the contents of the memory locations pointed to by 'valueA' and 'valueB'.
 */
void swapValues(int *valueA, int *valueB) {
    int temp = *valueA;

    *valueA = *valueB;
    *valueB = temp;
}

/*
 * Performs depth-first search to generate all permutations of an integer array.
 *
 * The 'dfs' function performs depth-first search to generate all permutations of an
 * integer array 'nums' of size 'numsSize'. It uses recursion to explore different
 * permutations, swapping elements at different indices and backtracking to explore all
 * possibilities. The 'curr' parameter keeps track of the current position being explored.
 * When the 'curr' value exceeds or is equal to 'numsSize - 1', a new permutation is added
 * to the 'permuted' array and the 'returnSize' is incremented. The 'returnColumnSizes'
 * array is updated to store the size of each generated permutation.
 *
 * Parameters:
 * - nums: A pointer to an array of integers to be permuted.
 * - numsSize: The number of elements in the array.
 * - permuted: A pointer to a pointer to an array of integer arrays for storing permutations.
 * - returnSize: A pointer to an integer storing the number of permutations generated.
 * - returnColumnSizes: A pointer to an array storing the sizes of each generated permutation.
 * - curr: The current position being explored during recursion.
 *
 * This function efficiently generates all permutations of the input integer array by
 * using depth-first search and backtracking. It populates the 'permuted' array and updates
 * the 'returnSize' and 'returnColumnSizes' arrays to store the generated permutations.
 */
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

/*
 * Generates all permutations of an integer array.
 *
 * The 'permute' function generates all permutations of an integer array 'nums' of size
 * 'numsSize' using depth-first search. It initializes the 'returnSize' to store the
 * number of generated permutations. It calculates the total number of permutations as
 * 'numsSize!' and allocates memory for the 'permutedArray' and 'returnColumnSizes' arrays.
 * The function then calls the 'dfs' function to generate all permutations and populates
 * the 'permutedArray' and 'returnColumnSizes' arrays. The generated permutations are
 * stored in 'permutedArray' and the sizes of each permutation are stored in
 * 'returnColumnSizes'.
 *
 * Parameters:
 * - nums: A pointer to an array of integers to be permuted.
 * - numsSize: The number of elements in the array.
 * - returnSize: A pointer to an integer storing the number of permutations generated.
 * - returnColumnSizes: A pointer to an array storing the sizes of each generated permutation.
 *
 * Returns:
 * A pointer to a pointer to an array of integer arrays containing all generated permutations.
 *
 * This function efficiently generates and returns all permutations of the input integer
 * array using depth-first search and backtracking. It also updates the 'returnSize' and
 * 'returnColumnSizes' arrays to store the sizes of the generated permutations.
 */
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
