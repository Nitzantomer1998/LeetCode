class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Check if a given integer is a power of two.

        Args:
            n (int): An integer.

        Returns:
            bool: True if the given integer is a power of two, False otherwise.

        Time Complexity: o(1) since we are only make a 2 comparisons.
        Space Complexity: o(1) since we are not using any additional space.
        """
        isPositive = n > 0
        isTwoPower = n & (n - 1) == 0

        return isPositive and isTwoPower