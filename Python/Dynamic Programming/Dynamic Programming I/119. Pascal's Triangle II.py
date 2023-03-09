def get_row(row_index: int) -> list[int]:
   
    pascal_triangle = [[1] * (i + 1) for i in range(row_index + 1)]

    for row in range(2, row_index + 1):
        for col in range(1, row):
            pascal_triangle[row][col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]

    return pascal_triangle[-1]
