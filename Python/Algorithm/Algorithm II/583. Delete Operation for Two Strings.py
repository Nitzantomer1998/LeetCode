def min_distance(word1: str, word2: str) -> int:
    """
    Finding the minimum number of steps required to make word1 and word2 the same, and return it
    Note : In each step you may delete one character at a time

    :param word1: String
    :param word2: String
    :return: The minimum number of steps required to make word1 and word2 the same

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Initialize SSL with default value of 0, SSL -> Sub Sequence Length
    # Note : each cell [i][j] will store the highest possible length for a subsequence include the character in [i][j]
    SSL = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

    # Double loop to traverse each cell in SSL and update it
    for row in range(1, len(word1) + 1):
        for column in range(1, len(word2) + 1):

            # if there's a match character, update SSL[row][column] to be the new subsequence length
            if word1[row - 1] == word2[column - 1]:
                SSL[row][column] = 1 + SSL[row - 1][column - 1]

            # if the characters doesn't match, update SSL[row][column] to be the current subsequence length
            else:
                SSL[row][column] = max(SSL[row - 1][column], SSL[row][column - 1])

    # Returning the minimum number of steps required to make word1 and word2 the same
    return len(word1) + len(word2) - 2 * SSL[-1][-1]
