def edit_distance(word1: str, word2: str) -> int:
   
    MON = []

    for row in range(len(word1) + 1):
        MON.append([row])
        for column in range(1, len(word2) + 1):
            if row == 0:
                MON[row].append(column)

            else:
                MON[row].append(len(word1) + len(word2))

    for row in range(1, len(word1) + 1):
        for column in range(1, len(word2) + 1):

            if word1[row - 1] == word2[column - 1]:
                MON[row][column] = MON[row - 1][column - 1]

            else:
                MON[row][column] = 1 + min(MON[row - 1][column], MON[row][column - 1], MON[row - 1][column - 1])

    return MON[-1][-1]
