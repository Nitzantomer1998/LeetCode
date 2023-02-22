from collections import defaultdict


def max_points(points: list[list[int]]) -> int:
    """
    Finding the maximum number of points that lie on the same straight line, and return it

    :param points: List in List of integers, represent points on graph
    :return: The maximum number of points that lie on the same straight line

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """

    # Assisting function for more readability code
    def find_slope(p1: list, p2: list) -> float:
        """
        Finding the slope between the two points, and return it

        :param p1: Points
        :param p2: Points
        :return: the slope between the two points
        """
        # Unpacking for nicer code
        x1, y1 = p1
        x2, y2 = p2

        # if both x's are equals, then we get error of 0 division, therefore return infinity
        if x1 == x2:
            return float('infinity')

        # Returning the slope between the points
        return (y1 - y2) / (x1 - x2)

    # MPOL -> Max Points On Line, integer storing the maximum points on the same line
    MPOL = 0

    # Loop to travers each points in the list
    for i in range(len(points)):

        # Creating slopes dictionary for counting each points on the calculated slop
        slopes = defaultdict(int)

        # Loop to traverse on points, and calculate each slope
        for j in range(i + 1, len(points)):
            # Getting the slope between the two points
            slope = find_slope(points[i], points[j])

            # Increase the slope counter in the dictionary
            slopes[slope] += 1

            # Update the maximum number of points on a possible slope
            MPOL = max(slopes[slope], MPOL)

    # Returning the maximum number of points that lie on the same straight line
    return MPOL + 1
