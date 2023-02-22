from collections import defaultdict


def max_points(points: list[list[int]]) -> int:
    
    def find_slope(p1: list, p2: list) -> float:
        
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            return float('infinity')

        return (y1 - y2) / (x1 - x2)

    MPOL = 0

    for i in range(len(points)):

        slopes = defaultdict(int)

        for j in range(i + 1, len(points)):
            slope = find_slope(points[i], points[j])

            slopes[slope] += 1

            MPOL = max(slopes[slope], MPOL)

    return MPOL + 1
