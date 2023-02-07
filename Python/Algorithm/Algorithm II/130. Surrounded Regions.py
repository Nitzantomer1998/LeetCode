def solve(board: list[list[str]]) -> None:
    
    MAX_ROW = len(board)
    MAX_COLUMN = len(board[0])

    def capture(row: int, column: int) -> None:
        
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or board[row][column] != 'O':
            return

        board[row][column] = 'T'

        capture(row - 1, column)
        capture(row + 1, column)
        capture(row, column - 1)
        capture(row, column + 1)

    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):
            if board[row][column] == 'O' and (row in [0, MAX_ROW - 1] or column in [0, MAX_COLUMN - 1]):
                capture(row, column)

    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):

            if board[row][column] == 'O':
                board[row][column] = 'X'

            elif board[row][column] == 'T':
                board[row][column] = 'O'
