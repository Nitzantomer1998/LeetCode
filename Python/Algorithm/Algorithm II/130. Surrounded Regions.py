class Solution:

    def isValidCell(self, board: list[list[int]], row: int, column: int) -> bool:
        """
        Check if a cell is a valid cell within the board.

        Args:
            board (List[List[int]]): The board represented as a list of lists of integers.
            row (int): The row index of the cell.
            column (int): The column index of the cell.

        Returns:
            bool: True if the cell is valid, False otherwise.
        """
        ROWS = len(board)
        COLUMNS = len(board[0])

        isValidRow = 0 <= row < ROWS
        isValidColumn = 0 <= column < COLUMNS

        return isValidRow and isValidColumn

    def dfs(self, board: list[list[int]], row: int, column: int) -> None:
        """
        Perform Depth-First Search (DFS) to mark connected 'O' cells as 'U'.

        Args:
            board (List[List[int]]): The board represented as a list of lists of integers.
            row (int): The current row index.
            column (int): The current column index.

        Returns:
            None
        """
        if self.isValidCell(board, row, column) == False:
            return
        
        if board[row][column] != 'O':
            return
        
        board[row][column] = 'U'

        self.dfs(board, row - 1, column)
        self.dfs(board, row + 1, column)
        self.dfs(board, row, column - 1)
        self.dfs(board, row, column + 1)

    def solve(self, board: list[list[str]]) -> None:
        """
        Solve the 'Surrounded Regions' problem by capturing surrounded regions.

        Args:
            board (List[List[str]]): The board represented as a list of lists of characters.

        Returns:
            None
        """
        ROWS = len(board)
        COLUMNS = len(board[0])

        for row in range(ROWS):
            for column in range(COLUMNS):
                if row in [0, ROWS - 1] or column in [0, COLUMNS - 1]:
                    if board[row][column] == 'O':
                        self.dfs(board, row, column)

        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == 'O':
                    board[row][column] = 'X'

                elif board[row][column] == 'U':
                    board[row][column] = 'O'
