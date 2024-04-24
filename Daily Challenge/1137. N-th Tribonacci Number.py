class Solution:
    def tribonacci(self, n: int) -> int:
        triArray = [0, 1, 1]

        for _ in range(n - 2):
            triArray[0], triArray[1], triArray[2] = triArray[1], triArray[2], sum(triArray)

        return triArray[n] if n < 3 else triArray[2]
        
