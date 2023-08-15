/**
 * Generates all possible letter case permutations of a string.
 *
 * The 'backtrack' function generates all possible letter case permutations
 * of the input string 's' by recursively filling the 'currentPermutation'
 * array. It stores the generated permutations in 'permutatedArray' and
 * updates the 'returnSize'.
 *
 * Parameters:
 * - s: The input string for which to generate letter case permutations.
 * - index: The current index being processed in the string.
 * - currentPermutation: The current permutation being generated.
 * - permutatedArray: An array to store the generated permutations.
 * - returnSize: A pointer to the variable that stores the number of permutations.
 */
void backtrack(char* s, int index, char* currentPermutation, char** permutatedArray, int* returnSize) {
    if (index == strlen(s)) {
        permutatedArray[*returnSize] = strdup(currentPermutation);
        (*returnSize)++;
        return;
    }
    
    currentPermutation[index] = tolower(s[index]);
    backtrack(s, index + 1, currentPermutation, permutatedArray, returnSize);

    if (isalpha(s[index])) {
        currentPermutation[index] = toupper(s[index]);
        backtrack(s, index + 1, currentPermutation, permutatedArray, returnSize);
    }
}

/**
 * Generates all possible letter case permutations of a string.
 *
 * The 'letterCasePermutation' function generates all possible letter case permutations
 * of the input string 's'. It uses the 'backtrack' helper function to fill the
 * 'permutatedArray' with the computed permutations.
 *
 * Parameters:
 * - s: The input string for which to generate letter case permutations.
 * - returnSize: A pointer to the variable that will store the number of permutations.
 *
 * Returns:
 * A 2D array containing all possible letter case permutations of the input string.
 */
char **letterCasePermutation(char * s, int* returnSize) {
    int stringLength = strlen(s);
    int totalPermutations = 1 << stringLength;
    
    char** permutatedArray = (char**) malloc (sizeof(char*) * totalPermutations);
    for (int row = 0; row < totalPermutations; row++) {
        permutatedArray[row] = (char*) malloc (sizeof(char) * (stringLength + 1));
        permutatedArray[row][stringLength] = '\0';
    }
    
    char* currentPermutation = (char*) malloc (sizeof(char) * (stringLength + 1));
    currentPermutation[stringLength] = '\0';
    
    *returnSize = 0;
    backtrack(s, 0, currentPermutation, permutatedArray, returnSize);
    
    free(currentPermutation);
    return permutatedArray;
}
