import sys


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    
    previous_row_min_sum = [sys.maxsize] * len(matrix)

    for i in range(len(matrix)):

        current_row_min_sum = [sys.maxsize] * len(matrix)

        for j in range(len(matrix)):

            if i == 0:
                current_row_min_sum[j] = matrix[i][j]

            else:
                if j > 0:
                    current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j - 1] + matrix[i][j])
                current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j] + matrix[i][j])
                if j < len(matrix) - 1:
                    current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j + 1] + matrix[i][j])

        previous_row_min_sum = current_row_min_sum

    return min(previous_row_min_sum)
