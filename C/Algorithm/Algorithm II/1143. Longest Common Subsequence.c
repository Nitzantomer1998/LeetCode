#include <string.h>
#include <stdlib.h>

/* Definition for getting the maximum value */
#define MAX(X, Y) (X > Y ? X : Y)

/*
 * Calculates the length of the longest common subsequence of two strings.
 *
 * The 'longestCommonSubsequence' function takes two strings 'textA' and 'textB' as input
 * and calculates the length of the longest common subsequence between these two strings using
 * dynamic programming. It returns the length of the longest common subsequence.
 *
 * Parameters:
 * - textA: The first input string.
 * - textB: The second input string.
 *
 * Returns:
 * The length of the longest common subsequence.
 */
int longestCommonSubsequence(char *textA, char *textB)
{
    int A_LENGTH = strlen(textA) + 1;
    int B_LENGTH = strlen(textB) + 1;

    int **commonSubsequence = (int **)calloc(A_LENGTH, sizeof(int *));
    for (int row = 0; row < A_LENGTH; row++)
        commonSubsequence[row] = (int *)calloc(B_LENGTH, sizeof(int));

    for (int row = 1; row < A_LENGTH; row++)
    {
        for (int column = 1; column < B_LENGTH; column++)
        {
            if (textA[row - 1] == textB[column - 1])
                commonSubsequence[row][column] = commonSubsequence[row - 1][column - 1] + 1;
            else
                commonSubsequence[row][column] = MAX(commonSubsequence[row - 1][column], commonSubsequence[row][column - 1]);
        }
    }

    return commonSubsequence[A_LENGTH - 1][B_LENGTH - 1];
}
