from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number in an array where every element appears twice except for one.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The single number.

        Time Complexity: o(n) where n is the number of elements in the array.
        Space Complexity: o(1)
        """
        uniqueValue = 0
    
        for value in nums:
            uniqueValue ^= value

        return uniqueValue
