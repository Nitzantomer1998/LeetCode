def min_cost_climbing_stairs(cost: list[int]) -> int:
    
    for index in range(2, len(cost)):
        cost[index] += min(cost[index - 1], cost[index - 2])

    return min(cost[-1], cost[-2])
