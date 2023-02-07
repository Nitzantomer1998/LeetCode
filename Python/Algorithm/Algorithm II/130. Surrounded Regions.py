def solve(board: list[list[str]]) -> None:
    """
    Modifying the matrix such that every region that surround by X will update to X as well
    Note : Region is a group of 4-directionally with the value O that surrounded by 'X'

    :param board: Matrix contain X and O
    :return: Nothing, None, Everything happen in place

    Time Complexity: o(n * m)
    Space Complexity: o(n * m)
    """
    # Constants for the cells indices boundaries, for more readable code
    MAX_ROW = len(board)
    MAX_COLUMN = len(board[0])

    # Assisting function to make the DFS calls
    def capture(row: int, column: int) -> None:
        """
        Recursive function for checking if the current indices is part or a region using DFS Algorithm

        :param row: Integer represent the current cell row
        :param column: Integer represent the current cell column
        :return: None, Everything happen in place
        """
        # if the sent indices are invalid or the cell is not part of the region, return
        if not (0 <= row < MAX_ROW and 0 <= column < MAX_COLUMN) or board[row][column] != 'O':
            return

        # the current cell is part of the region, update it to special symbol T
        board[row][column] = 'T'

        # 4 Callbacks to the other possible regions in the horizontal vertical axis
        capture(row - 1, column)
        capture(row + 1, column)
        capture(row, column - 1)
        capture(row, column + 1)

    # 1. (DFS) Capture un-surrounded regions and update value (O -> T)
    # Traverse the border, if there's O check for region and update their values for T (symbol for un-surrounded)
    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):
            if board[row][column] == 'O' and (row in [0, MAX_ROW - 1] or column in [0, MAX_COLUMN - 1]):
                capture(row, column)

    # 2. Capture surrounded regions and update value (O -> X), also update un-surrounded regions (T -> O)
    for row in range(MAX_ROW):
        for column in range(MAX_COLUMN):

            if board[row][column] == 'O':
                board[row][column] = 'X'

            elif board[row][column] == 'T':
                board[row][column] = 'O'
