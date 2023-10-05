import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
            s (str): Input string.

        Returns:
            int: Length of the longest substring without repeating characters.

        Time Complexity: o(n^2) where n is the length of the input string.
        Space Complexity: o(n) where n is the length of the input string.
        """
        longestSubstring = 0
                
        currentWindow = collections.OrderedDict()    
        
        for index, char in enumerate(s):
            while char in currentWindow:
                currentWindow.popitem(last=False)
            
            longestSubstring = max(longestSubstring, len(currentWindow) + 1)
            currentWindow[char] = index

        return longestSubstring
