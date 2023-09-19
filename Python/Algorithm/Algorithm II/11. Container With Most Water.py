from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum area between two bars in a container.

        Args:
            heightList (List[int]): A list of integers representing the heights of the bars.

        Returns:
            int: The maximum area between two bars in the container.
        """
        HEIGHT_LENGTH = len(height)

        maxContainer = 0

        leftPointer = 0
        rightPointer = HEIGHT_LENGTH - 1

        while leftPointer < rightPointer:
            leftBar = height[leftPointer]
            rightBar = height[rightPointer]
            barDistance = rightPointer - leftPointer

            currentContainer = min(leftBar, rightBar) * barDistance
            maxContainer = max(maxContainer, currentContainer)

            if leftBar < rightBar:
                leftPointer += 1
            else:
                rightPointer -= 1

        return maxContainer
