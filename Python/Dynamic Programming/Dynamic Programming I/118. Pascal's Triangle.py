def generate(num_rows: int) -> list[list[int]]:
    
    pascal_triangle = [[1] * (i + 1) for i in range(num_rows)]

    for row in range(2, num_rows):
        for col in range(1, row):
            pascal_triangle[row][col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]

    return pascal_triangle
