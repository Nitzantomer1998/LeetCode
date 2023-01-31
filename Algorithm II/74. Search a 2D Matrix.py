def search_matrix(matrix: list[list[int]], target: int) -> bool:
    
    up, down = 0, len(matrix) - 1

    while up <= down:

        middle_row = (up + down) // 2

        if matrix[middle_row][0] <= target <= matrix[middle_row][-1]:

            left, right = 0, len(matrix[middle_row]) - 1

            while left <= right:

                middle_index = (left + right) // 2

                if matrix[middle_row][middle_index] == target:
                    return True

                elif matrix[middle_row][middle_index] > target:
                    right = middle_index - 1

                else:
                    left = middle_index + 1

            return False

        elif matrix[middle_row][-1] > target:
            down = middle_row - 1

        else:
            up = middle_row + 1
