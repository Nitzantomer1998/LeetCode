def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Checking if target in matrix, and return accordingly
    Note : Matrix rows and cells are in ascending order such that matrix[row][-1] < matrix[row + 1][-1]

    :param matrix: Matrix that every row and cell in ascending order
    :param target: Integer we are searching for in matrix
    :return: True if target in matrix, else False

    Time Complexity: o(log(log(n)))
    Space Complexity: o(1)
    """
    # First binary search : Finding the needed row of matrix
    # Up & Down pointer to traverse the sorted rows of the matrix (Up = first row, Down = last row)
    up, down = 0, len(matrix) - 1

    # Loop to traverse the matrix row
    while up <= down:

        # Integer storing the middle row index
        middle_row = (up + down) // 2

        # if target is in the middle row
        # secondary binary search : Finding the needed index of target in middle_row
        if matrix[middle_row][0] <= target <= matrix[middle_row][-1]:

            # Left & Right pointer to traverse the sorted middle_row
            left, right = 0, len(matrix[middle_row]) - 1

            # Loop to traverse the matrix cells of the middle_row
            while left <= right:

                # Integer storing the middle index of middle_row
                middle_index = (left + right) // 2

                # if we found target, return True
                if matrix[middle_row][middle_index] == target:
                    return True

                # if current middle value is bigger than target, update right to be middle_index - 1
                elif matrix[middle_row][middle_index] > target:
                    right = middle_index - 1

                # if current middle value is smaller than target, update left to be middle_index + 1
                else:
                    left = middle_index + 1

            # if we end the second binary search than the target doesn't exist in matrix, return False
            return False

        # if current middle row last cell is bigger than target, update down to be middle_index - 1
        elif matrix[middle_row][-1] > target:
            down = middle_row - 1

        # if current middle row last cell is smaller than target, update up to be middle_index + 1
        else:
            up = middle_row + 1
