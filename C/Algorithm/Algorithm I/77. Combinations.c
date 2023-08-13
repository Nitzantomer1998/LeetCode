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
