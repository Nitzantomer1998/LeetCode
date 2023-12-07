class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        """
        Check if any permutation of string s1 is a substring of string s2.

        Args:
            s1 (str): The first input string.
            s2 (str): The second input string.

        Returns:
            bool: True if any permutation of s1 is a substring of s2, False otherwise.

        Time Complexity: o(n) where n is the length of the bigger string.
        Space Complexity: o(1) since we are using a fixed size array of 26 characters.
        """
        STRING_ONE_LENGTH = len(s1)

        stringOneContent = [0] * 26
        stringTwoContent = [0] * 26

        for char in s1:
            stringOneContent[ord(char) - ord('a')] += 1

        for index, char in enumerate(s2):
            if index >= STRING_ONE_LENGTH:
                stringTwoContent[ord(s2[index - STRING_ONE_LENGTH]) - ord('a')] -= 1

            stringTwoContent[ord(char) - ord('a')] += 1

            if stringOneContent == stringTwoContent:
                return True

        return False