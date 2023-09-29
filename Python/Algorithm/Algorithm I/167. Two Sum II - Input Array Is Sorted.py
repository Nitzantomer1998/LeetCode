from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted array that add up to a specific target.

        Args:
            numbers (List[int]): A list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two numbers that add up to the target.
        """
        NUMBERS_LENGTH = len(numbers)

        leftPointer = 0
        rightPointer = NUMBERS_LENGTH - 1

        while leftPointer < rightPointer:
            currentSum = numbers[leftPointer] + numbers[rightPointer]

            if currentSum == target:
                return [leftPointer + 1, rightPointer + 1]

            elif currentSum < target:
                leftPointer += 1

            else:
                rightPointer -= 1
