from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Creating all the possible combinations of length k chosen from the range [1, n], and return it.

        Args:
            n (int): An integer representing the highest digit value allowed.
            k (int): An integer representing the permutation needed length.
        
        Returns:
            List[List[int]]: All the possible combinations.

        Time Complexity: o(nCk) where n is the highest digit value allowed, and k is the permutation length.
        Space Complexity: o(n * k) since we are using a list to store all the possible combinations.
        """
        MAX_VALUE = n + 1
        PERMUTATION_LENGTH = k

        permutationSolution = []

        for digit in range(1, MAX_VALUE):
            self.addNthPremutation(digit, [digit], permutationSolution, PERMUTATION_LENGTH, MAX_VALUE)

        return permutationSolution

    def addNthPremutation(self, currentDigit: int, currentPermutation: List[int], permutationSolution: List[List[int]], PERMUTATION_LENGTH: int, MAX_VALUE: int) -> None:
        """
        Adding the possible permutation for the current index.

        Args:
            currentDigit (int): Integer representing the digit we are at.
            currentPermutation (List[int]): List representing the current built permutation.
            permutationSolution (List[List[int]]): List to store all the possible permutations.
            PERMUTATION_LENGTH (int): Integer representing the permutation needed length.
            MAX_VALUE (int): Integer representing the highest digit value allowed.

        Returns:
            None: Everything happens in place.

        Time Complexity: o((n - currentDigit) ^ k) where n is the range, k is the length of combinations, and currentDigit ranges from 1 to n.
        Space Complexity: o(k + n ^ k) where k is the length of combinations, and the recursion stack uses space proportional to the length of the combinations being generated.
        """
        CURRENT_PERMUTATION_LENGTH = len(currentPermutation)

        if CURRENT_PERMUTATION_LENGTH == PERMUTATION_LENGTH:
            permutationSolution.append(currentPermutation[:])
            return

        for nextDigit in range(currentDigit + 1, MAX_VALUE):
            self.addNthPremutation(nextDigit, currentPermutation + [nextDigit], permutationSolution, PERMUTATION_LENGTH, MAX_VALUE)
