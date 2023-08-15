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
