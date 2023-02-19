def edit_distance(word1: str, word2: str) -> int:
    """
    Finding the minimum number of operations required to convert word1 to word2, and return it
    Note : The available operations are Insert / Delete / Replace, each one cost value is 1

    :param word1: String
    :param word2: String
    :return: The minimum number of operations required to convert word1 to word2

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Initialize MON with default value of 0, MON -> Minimum Operation Needed
    # Note : each cell [i][j] will store the minimum needed operation till this index from start
    MON = []

    # Initialize MON, The first Row and Column store the base cases, the others store default value of maximum number
    for row in range(len(word1) + 1):
        MON.append([row])
        for column in range(1, len(word2) + 1):
            if row == 0:
                MON[row].append(column)

            else:
                MON[row].append(len(word1) + len(word2))

    # Double loop to traverse each cell in MON and update it
    for row in range(1, len(word1) + 1):
        for column in range(1, len(word2) + 1):

            # if the characters match than no needed to execute an operation therefore number of operation is the same
            if word1[row - 1] == word2[column - 1]:
                MON[row][column] = MON[row - 1][column - 1]

            # if the characters doesn't match, update MON[row][column] to be the minimum needed operation
            else:
                MON[row][column] = 1 + min(MON[row - 1][column], MON[row][column - 1], MON[row - 1][column - 1])

    # Returning the minimum number of operations required to convert word1 to word2
    return MON[-1][-1]
