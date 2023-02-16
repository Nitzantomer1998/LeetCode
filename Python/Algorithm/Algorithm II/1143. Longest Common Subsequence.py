def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Finding the length of the longest common subsequence of text1 in text2, and return it

    :param text1: String
    :param text2: String
    :return: The length of the longest common subsequence of text1 in text2

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Initialize SSL with default value of 0, SSL -> Sub Sequence Length
    # Note : each cell [i][j] will store the highest possible length for a subsequence include the character in [i][j]
    SSL = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    # Double loop to traverse each cell in SSL and update it
    for row in range(1, len(text1) + 1):
        for column in range(1, len(text2) + 1):

            # if there's a match character, update SSL[row][column] to be the new subsequence length
            if text1[row - 1] == text2[column - 1]:
                SSL[row][column] = 1 + SSL[row - 1][column - 1]

            # if the characters doesn't match, update SSL[row][column] to be the current subsequence length
            else:
                SSL[row][column] = max(SSL[row - 1][column], SSL[row][column - 1])

    # Returning the maximum sequence length
    return SSL[-1][-1]
