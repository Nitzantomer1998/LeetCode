def maximal_square(matrix: list[list[str]]) -> int:
    
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    max_square_size = [[0] * cols for _ in range(rows)]

    max_size = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '0':
                max_square_size[i][j] = 0

            else:
                if i == 0 or j == 0:
                    max_square_size[i][j] = 1

                else:
                    max_square_size[i][j] = min(max_square_size[i - 1][j], max_square_size[i][j - 1],
                                                max_square_size[i - 1][j - 1]) + 1

                max_size = max(max_size, max_square_size[i][j])

    return max_size * max_size
