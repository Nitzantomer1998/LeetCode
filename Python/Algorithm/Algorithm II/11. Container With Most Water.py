from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
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
