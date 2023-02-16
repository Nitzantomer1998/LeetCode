def longest_common_subsequence(text1: str, text2: str) -> int:
    
    SSL = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for row in range(1, len(text1) + 1):
        for column in range(1, len(text2) + 1):

            if text1[row - 1] == text2[column - 1]:
                SSL[row][column] = 1 + SSL[row - 1][column - 1]

            else:
                SSL[row][column] = max(SSL[row - 1][column], SSL[row][column - 1])

    return SSL[-1][-1]
