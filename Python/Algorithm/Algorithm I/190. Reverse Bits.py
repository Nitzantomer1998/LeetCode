class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.

        Args:
            n (int): A 32-bit unsigned integer.

        Returns:
            int: The integer with reversed bits.

        Time Complexity: o(1) since we are only looping 32 times.
        Space Complexity: o(1) since we are not using any additional space.
        """
        reversedValue = 0

        for _ in range(32):
            bitValue = (n & 1)
            reversedValue = (reversedValue << 1) + bitValue
            n >>= 1

        return reversedValue
