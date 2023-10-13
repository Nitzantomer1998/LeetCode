import collections
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all the zeroes in the given list to the end while maintaining the order of other elements.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            None: The function modifies the input list in-place.

        Time Complexity: o(n) where n is the length of the given list.
        Space Complexity: o(n) where n is the length of the given list.
        """
        NUMS_LENGTH = len(nums)
        zerosIndex = collections.deque()

        for index in range(NUMS_LENGTH):
            if nums[index]:
                if zerosIndex:
                    newIndex = zerosIndex.popleft()
                    nums[index], nums[newIndex] = nums[newIndex], nums[index]
                    zerosIndex.append(index)

            else:
                zerosIndex.append(index)
