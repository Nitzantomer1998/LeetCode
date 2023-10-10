from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate an array to the right by k steps in-place.

        Args:
            nums (List[int]): A list of integers.
            k (int): The number of steps to rotate.

        Returns:
            None

        Time Complexity: o(n) where n is the number of elements in the array.
        Space Complexity: o(1) since we are not using any additional space.
        """
        NUMS_LENGTH = len(nums)
        k = k % NUMS_LENGTH

        self.reverse(nums, 0, NUMS_LENGTH - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, NUMS_LENGTH - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        Reverse a portion of the array in-place.

        Args:
            nums (List[int]): A list of integers.
            start (int): The starting index for the reverse operation.
            end (int): The ending index for the reverse operation.

        Returns:
            None

        Time Complexity: o(n) where n is the number of elements in the array from start to end.
        Space Complexity: o(1)
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
