def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    Find the minimum cost to reach the top of the floor, and return it
    Note : From each stair you may either make 1 step or 2

    :param cost: List of integers, each cell represent the cost of the step
    :return: The minimum cost to reach the top of the floor

    Time Complexity: o(n)
    Space Complexity: o(1)
    """
    # Loop to traverse each stair in cost
    for index in range(2, len(cost)):
        # Updating the cost of the current stair to be the current + the minimum cost to get to it
        cost[index] += min(cost[index - 1], cost[index - 2])

    # Returning the minimum cost to reach to the top floor
    return min(cost[-1], cost[-2])
