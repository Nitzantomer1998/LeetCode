def minimum_total(triangle: list[list[int]]) -> int:
    
    for row in reversed(range(len(triangle))):

        for column in range(len(triangle[row]) - 1):
            first_option = triangle[row - 1][column] + triangle[row][column]
            second_option = triangle[row - 1][column] + triangle[row][column + 1]

            triangle[row - 1][column] = min(first_option, second_option)

    return triangle[0][0]
