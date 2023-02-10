def exist(board: list[list[str]], word: str) -> bool:
   
    MAX_ROW = len(board)
    MAX_COLUMN = len(board[0])
    MAX_WORD = len(word)

    def is_word_exist(row: int, column: int, word_index: int) -> bool:
        
        if word_index == MAX_WORD:
            return True

        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or board[row][column] != word[word_index]:
            return False

        if board[row][column] != word[word_index]:
            return False

        board[row][column] = '#'

        is_word_found = is_word_exist(row + 1, column, word_index + 1) or is_word_exist(row - 1, column,
                                                                                        word_index + 1) or is_word_exist(
            row, column + 1, word_index + 1) or is_word_exist(row, column - 1, word_index + 1)

        board[row][column] = word[word_index]

        return is_word_found

    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):

            if is_word_exist(row, column, 0):
                return True

    return False
