/**
 * Calculates the factorial of a non-negative integer.
 *
 * The 'factorial' function calculates the factorial of a non-negative integer 'value'
 * using a recursive approach and memoization. It returns the result of the factorial computation.
 *
 * Parameters:
 * - value: The non-negative integer for which to calculate the factorial.
 * - factorialMemo: An array to store precomputed factorial values.
 *
 * Returns:
 * The factorial of the input 'value'.
 */
long factorial(int value, long* factorialMemo) {
    if (value < 2)
        return 1;
    
    if (factorialMemo[value] != -1)
        return factorialMemo[value];

    factorialMemo[value] = value * factorial(value - 1, factorialMemo);
    return factorialMemo[value];
}

/**
 * Generates combinations of 'k' elements from 'n' distinct integers using a recursive approach.
 *
 * The 'generateCombinations' function is a helper function used by the 'combine' function to
 * generate all possible combinations of 'k' elements from a set of 'n' distinct integers.
 * It uses a recursive approach and memoization to fill the 'combinationsArray' with the computed combinations.
 *
 * Parameters:
 * - combinationsArray: A pointer to the 2D array that will store the generated combinations.
 * - index: A pointer to the current index in the 'combinationsArray' being processed.
 * - data: An array used to store intermediate combination values during recursion.
 * - start: The starting point for generating combinations.
 * - n: The total number of distinct integers available for combinations.
 * - k: The size of each combination to generate.
 * - pos: The current position in the 'data' array during recursion.
 */
void generateCombinations(int** combinationsArray, int* index, int* data, int start, int n, int k, int pos) {
    if (pos == k) {
        memcpy(combinationsArray[*index], data, sizeof(int) * k);
        (*index)++;
        return;
    }

    for (int i = start; i <= n - (k - pos) + 1; i++) {
        data[pos] = i;
        generateCombinations(combinationsArray, index, data, i + 1, n, k, pos + 1);
    }
}

/**
 * Generates combinations of 'k' elements from 'n' distinct integers.
 *
 * The 'combine' function generates all possible combinations of 'k' elements from a set
 * of 'n' distinct integers. It uses a recursive approach and memoization to fill the
 * 'combinationsArray' with the computed combinations. The sizes of the combinations
 * are stored in 'returnColumnSizes'.
 *
 * Parameters:
 * - n: The total number of distinct integers available for combinations.
 * - k: The size of each combination to generate.
 * - returnSize: A pointer to the variable that will store the number of generated combinations.
 * - returnColumnSizes: An array to store the sizes of each generated combination.
 *
 * Returns:
 * A 2D array containing all possible combinations of 'k' elements from 'n' integers.
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;

    if (n <= 0 || k <= 0 || k > n)
        return NULL;

    long* factorialMemo = (long*) malloc (sizeof(long) * (n + 1));
    for (int i = 0; i <= n; i++)
        factorialMemo[i] = -1;

    long combinationsSize = factorial(n, factorialMemo) / (factorial(k, factorialMemo) * factorial(n - k, factorialMemo));

    int** combinationsArray = (int**) malloc (sizeof(int*) * combinationsSize);
    int* columnSizes = (int*) malloc (sizeof(int) * combinationsSize);

    for (int row = 0; row < combinationsSize; row++) {
        combinationsArray[row] = (int*) malloc (sizeof(int) * k);
        columnSizes[row] = k;
    }

    int* data = (int*) malloc (sizeof(int) * k);
    int index = 0;

    generateCombinations(combinationsArray, &index, data, 1, n, k, 0);

    free(data);
    free(factorialMemo);

    *returnColumnSizes = columnSizes;
    *returnSize = combinationsSize;
    
    return combinationsArray;
}
