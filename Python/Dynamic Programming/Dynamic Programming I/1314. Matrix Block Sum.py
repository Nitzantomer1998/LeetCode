def matrix_block_sum(mat, k):
    
    m, n = len(mat), len(mat[0])

    answer = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            r1, c1 = max(0, i - k), max(0, j - k)
            r2, c2 = min(m - 1, i + k), min(n - 1, j + k)

            sub_matrix_sum = 0
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    sub_matrix_sum += mat[r][c]

            answer[i][j] = sub_matrix_sum

    return answer
