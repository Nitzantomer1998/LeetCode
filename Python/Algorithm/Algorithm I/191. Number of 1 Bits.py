class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Count the number of '1' bits in the binary representation of an integer.

        Args:
            n (int): An integer.

        Returns:
            int: The number of '1' bits.

        Time Complexity: o(n) where n is the number of bits in the binary representation of the integer.
        Space Complexity: o(1) since we are not using any additional space.
        """
        oneBitCounter = 0

        while n > 0:
            LSB_Value = n & 1
            oneBitCounter += LSB_Value

            n >>= 1

        return oneBitCounter
