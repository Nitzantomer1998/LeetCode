def exist(board: list[list[str]], word: str) -> bool:
    """
    Finding if the sent word exist in the board, and return accordingly
    Note : You may proceed from a cell only by vertically or horizontally

    :param board: Matrix of characters
    :param word: List of characters
    :return: True if the word exist in the board, else False

    Time Complexity: o(n * m * 4 ^ word_length)
    Space Complexity: o(n * m * 4 ^ word_length)
    """
    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW = len(board)
    MAX_COLUMN = len(board[0])
    MAX_WORD = len(word)

    # Assisting function to make the DFS calls
    def is_word_exist(row: int, column: int, word_index: int) -> bool:
        """
        Recursive function for checking if the current indices match to the current word char using DFS Algorithm

        :param row: Integer represent the current cell row
        :param column: Integer represent the current cell column
        :param word_index: Integer represent the current cell in word
        :return: True if the current char in board and word was a match, else False
        """
        # if we found the word, return True
        if word_index == MAX_WORD:
            return True

        # if the sent indices are invalid, return False
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or board[row][column] != word[word_index]:
            return False

        # if the word doesn't match, return False
        if board[row][column] != word[word_index]:
            return False

        # Temporary changing the current cell value, so we won't traverse it backwards
        board[row][column] = '#'

        # Callback to the other 4 directions to mapping the board searching for word
        is_word_found = is_word_exist(row + 1, column, word_index + 1) or is_word_exist(row - 1, column,
                                                                                        word_index + 1) or is_word_exist(
            row, column + 1, word_index + 1) or is_word_exist(row, column - 1, word_index + 1)

        # Updating the current cell value, for the next callbacks
        board[row][column] = word[word_index]

        # Returning whether the word found in the board
        return is_word_found

    # Double loop to traverse every cell in the board
    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):

            # Run dfs for searching the word, and if found return True
            if is_word_exist(row, column, 0):
                return True

    # if we ended the code, then the word doesn't show on the board, return False
    return False
