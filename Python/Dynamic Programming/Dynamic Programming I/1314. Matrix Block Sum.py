def matrix_block_sum(mat, k):
    """
    Returns a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
    i - k <= r <= i + k,
    j - k <= c <= j + k, and
    (r, c) is a valid position in the matrix.

    :param mat: a list of lists of integers representing the input matrix
    :param k: an integer representing the size of the sub-matrices
    :return: a list of lists of integers representing the answer matrix

    Time Complexity: o(m * n * k ^ 2)
    Space Complexity: o(n * m)
    """

    # Get the number of rows and columns in the input matrix
    m, n = len(mat), len(mat[0])

    # Create a matrix of zeros to store the sums of the sub-matrices
    answer = [[0] * n for _ in range(m)]

    # Iterate over each element in the input matrix
    for i in range(m):
        for j in range(n):
            # Calculate the indices of the top-left and bottom-right corners
            # of the sub-matrix with center (i, j) and size (2*k+1) x (2*k+1)
            r1, c1 = max(0, i - k), max(0, j - k)
            r2, c2 = min(m - 1, i + k), min(n - 1, j + k)

            # Calculate the sum of all elements in the sub-matrix
            sub_matrix_sum = 0
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    sub_matrix_sum += mat[r][c]

            # Store the sum of the sub-matrix in the corresponding element of the answer matrix
            answer[i][j] = sub_matrix_sum

    # Returning list of lists of integers representing the answer matrix
    return answer
