from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Search for the target value in a sorted list. If the target is not found, return the index where it should be inserted.

        Args:
            nums (List[int]): A list of integers.
            target (int): The target value to search for.

        Returns:
            int: The index of the target value if found, or the index where it should be inserted.

        Time Complexity: o(log(n)) where n is the length of the input list.
        Space Complexity: o(1) since we are not using any additional space.
        """
        NUMS_LENGTH = len(nums)

        leftPointer = 0
        rightPointer = NUMS_LENGTH - 1

        while leftPointer <= rightPointer:
            middlePointer = leftPointer + (rightPointer - leftPointer) // 2
            middleValue = nums[middlePointer]

            if middleValue == target:
                return middlePointer

            elif middleValue < target:
                leftPointer = middlePointer + 1

            else:
                rightPointer = middlePointer - 1

        return rightPointer + 1
