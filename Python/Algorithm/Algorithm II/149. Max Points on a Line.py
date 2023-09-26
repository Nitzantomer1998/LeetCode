import collections
import fractions
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Find the maximum number of points on the same line that can be formed by given points.

        Args:
            points (List[List[int]]): A list of points represented as lists of coordinates [x, y].

        Returns:
            int: The maximum number of points on the same line.
        """
        POINTS_LENGTH = len(points)

        maxPoints = 0

        for i in range(POINTS_LENGTH):
            slopeDict = collections.defaultdict(int)
            localMax = 0

            for j in range(i + 1, POINTS_LENGTH):
                X1, Y1 = points[i]
                X2, Y2 = points[j]

                currentSlope = 'vertical' if X1 == X2 else fractions.Fraction(Y2 - Y1, X2 - X1)
                slopeDict[currentSlope] += 1
                localMax = max(localMax, slopeDict[currentSlope])

            maxPoints = max(maxPoints, localMax + 1)

        return maxPoints
