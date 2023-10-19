class Solution:
    def reverseWord(self, s: str, startIndex: int, endIndex: int) -> None:
        """
        Reverse the characters in the given string from startIndex to endIndex (inclusive).

        Args:
            s (str): The input string.
            startIndex (int): The starting index for the reversal.
            endIndex (int): The ending index for the reversal.

        Returns:
            None: The function modifies the input string in-place.

        Time Complexity: o(n) where n is the number of characters to be reversed.
        Space Complexity: o(1) since the reversal is performed in-place.
        """
        while startIndex < endIndex:
            s[startIndex], s[endIndex] = s[endIndex], s[startIndex]
            
            startIndex += 1
            endIndex -= 1

    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in the given string.

        Args:
            s (str): The input string.

        Returns:
            str: The string with reversed word order.

        Time Complexity: o(n) where n is the length of the given string.
        Space Complexity: o(n) where n is the length of the given string.
        """
        STRING_LENGTH = len(s)
        s = list(s)
        startIndex = 0

        for endIndex in range(STRING_LENGTH + 1):
            if endIndex == STRING_LENGTH or s[endIndex] == ' ':
                self.reverseWord(s, startIndex, endIndex - 1)
                startIndex = endIndex + 1

        return ''.join(s)
