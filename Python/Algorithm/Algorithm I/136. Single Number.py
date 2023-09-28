from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Find the single number in an array where every element appears twice except for one.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The single number.
        """
        uniqueValue = 0
    
        for value in nums:
            uniqueValue ^= value

        return uniqueValue
