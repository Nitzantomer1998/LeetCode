from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determine if a string can be segmented into words from a given dictionary.

        Args:
            s (str): The input string to be segmented.
            wordDict (List[str]): A list of words in the dictionary.

        Returns:
            bool: True if the string can be segmented into words from the dictionary, False otherwise.
        """
        STRING_LENGTH = len(s)

        isWordMatch = [False] * (STRING_LENGTH + 1)
        isWordMatch[STRING_LENGTH] = True

        for stringIndex in range(STRING_LENGTH, -1, -1):
            for word in wordDict:
                WORD_LENGTH = len(word)

                if WORD_LENGTH + stringIndex <= STRING_LENGTH:
                    if word == s[stringIndex: stringIndex + WORD_LENGTH]:
                        isWordMatch[stringIndex] = isWordMatch[stringIndex + WORD_LENGTH]

                    if isWordMatch[stringIndex]:
                        break

        return isWordMatch[0]
