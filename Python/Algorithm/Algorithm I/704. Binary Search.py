from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for the target value in a sorted list of integers using binary search.

        Args:
            nums (List[int]): A sorted list of integers.
            target (int): The target value to search for.
        
        Returns:
            int: The index of the target value if found, otherwise -1.

        Time Complexity: o(log(n)) where n is the length of the list.
        Space Complexity: o(1) since we only use three integer variables.
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

        return -1