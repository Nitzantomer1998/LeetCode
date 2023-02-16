def min_distance(word1: str, word2: str) -> int:
    
    SSL = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    for row in range(1, len(word1) + 1):
        for column in range(1, len(word2) + 1):

            if word1[row - 1] == word2[column - 1]:
                SSL[row][column] = 1 + SSL[row - 1][column - 1]

            else:
                SSL[row][column] = max(SSL[row - 1][column], SSL[row][column - 1])

    return len(word1) + len(word2) - 2 * SSL[-1][-1]
