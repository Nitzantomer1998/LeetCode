import sys


def min_falling_path_sum(matrix: list[list[int]]) -> int:
    """
    Find the minimum sum of any falling path through the matrix, and return it
    Note : Starting at row 0, and you allow only to go (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)

    :param matrix: a list of lists representing the input matrix
    :return: The minimum sum of any falling path through the matrix

    Time Complexity: o(n ^ 2)
    Space Complexity: o(n)
    """
    # Initialize the previous row min sum list with infinity values
    previous_row_min_sum = [sys.maxsize] * len(matrix)

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):

        # Create a new list to store the minimum falling path sum up to each element in the current row
        current_row_min_sum = [sys.maxsize] * len(matrix)

        # Iterate through the columns of the matrix
        for j in range(len(matrix)):

            # If this is the first row, the minimum falling path sum is simply the value of the element itself
            if i == 0:
                current_row_min_sum[j] = matrix[i][j]

            else:
                # Compute the minimum falling path sum to the current element by considering the three possible paths
                # from the previous row
                if j > 0:
                    current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j - 1] + matrix[i][j])
                current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j] + matrix[i][j])
                if j < len(matrix) - 1:
                    current_row_min_sum[j] = min(current_row_min_sum[j], previous_row_min_sum[j + 1] + matrix[i][j])

        # Update the dynamic programming list with the minimum falling path sum for the current row
        previous_row_min_sum = current_row_min_sum

    # Return the minimum falling path sum for the last row
    return min(previous_row_min_sum)
