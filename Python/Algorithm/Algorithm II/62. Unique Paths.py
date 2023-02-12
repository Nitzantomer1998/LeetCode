def unique_paths(m: int, n: int) -> int:
    
    nth_unique_paths = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for column in range(1, n):
            nth_unique_paths[row][column] = nth_unique_paths[row - 1][column] + nth_unique_paths[row][column - 1]

    return nth_unique_paths[-1][-1]
