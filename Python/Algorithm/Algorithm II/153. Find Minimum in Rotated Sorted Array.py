from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array.

        Args:
            nums (List[int]): A list of integers representing a rotated sorted array.

        Returns:
            int: The minimum element in the array.
        """
        NUMS_LENGTH = len(nums)

        left = 0
        right = NUMS_LENGTH - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[left] <= nums[middle]:
                if nums[left] <= nums[right]:
                    return nums[left]

                else:
                    left = middle + 1

            else:
                right = middle
