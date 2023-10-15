from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse a list of characters in-place.

        Args:
            s (List[str]): A list of characters.

        Returns:
            None: The function modifies the input list in-place.

        Time Complexity: o(n) where n is the length of the input list.
        Space Complexity: o(1) since we are not using any extra space.
        """
        STRING_LENGTH = len(s)

        startPointer = 0
        endPointer = STRING_LENGTH - 1

        while startPointer < endPointer:
            s[startPointer], s[endPointer] = s[endPointer], s[startPointer]

            startPointer += 1
            endPointer -= 1
