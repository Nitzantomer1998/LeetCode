#include <string.h>
#include <stdlib.h>

#define MAX(X, Y) (X > Y ? X : Y)

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
