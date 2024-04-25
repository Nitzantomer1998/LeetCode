class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for character in s:
            longest = 1
            currentIndex = ord(character) - ord('a')
            for previousIndex in range(26):
                if abs(currentIndex - previousIndex) <= k:
                    longest = max(longest, 1 + dp[previousIndex])
            dp[currentIndex] = max(dp[currentIndex], longest)
        return max(dp)
