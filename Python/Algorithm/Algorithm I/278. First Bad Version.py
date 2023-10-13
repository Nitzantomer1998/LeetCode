class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Find the first bad version in a series of versions using binary search.

        Args:
            n (int): The number of versions.

        Returns:
            int: The first bad version.

        Time Complexity: o(log(n)) where n is the number of versions.
        Space Complexity: o(1) since we are not using any additional space.
        """
        leftPointer = 1
        rightPointer = n

        while leftPointer <= rightPointer:
            middlePointer = leftPointer + (rightPointer - leftPointer) // 2

            if isBadVersion(middlePointer):
                rightPointer = middlePointer - 1
            else:
                leftPointer = middlePointer + 1

        return rightPointer + 1
