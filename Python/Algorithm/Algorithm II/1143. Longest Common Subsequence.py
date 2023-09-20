class Solution:
    def maxValue(self, valueA: int, valueB: int) -> int:
        """
        Find the maximum value between two integers.

        Args:
            valueA (int): The first integer.
            valueB (int): The second integer.

        Returns:
            int: The maximum value between valueA and valueB.
        """
        if valueA > valueB:
            return valueA
        
        else:
            return valueB

    def longestCommonSubsequence(self, textA: str, textB: str) -> int:
        """
        Find the length of the longest common subsequence between two strings.

        Args:
            textA (str): The first input string.
            textB (str): The second input string.

        Returns:
            int: The length of the longest common subsequence between textA and textB.
        """
        A_LENGTH = len(textA) + 1
        B_LENGTH = len(textB) + 1

        commonSubsequence = [[0 for column in range(B_LENGTH)] for row in range(A_LENGTH)]

        for row in range(1, A_LENGTH):
            for column in range(1, B_LENGTH):
                if textA[row - 1] == textB[column - 1]:
                    commonSubsequence[row][column] = commonSubsequence[row - 1][column - 1] + 1

                else:
                    commonSubsequence[row][column] = self.maxValue(
                        commonSubsequence[row - 1][column],
                        commonSubsequence[row][column - 1]
                    )

        return commonSubsequence[A_LENGTH - 1][B_LENGTH - 1]
