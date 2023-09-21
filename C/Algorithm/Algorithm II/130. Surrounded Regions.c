#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/*
 * Checks if a cell is a valid cell in the grid.
 *
 * The 'isValidCell' function takes the row and column indices of a cell, as well as the total
 * number of rows ('ROWS') and columns ('COLUMNS') in the grid. It returns 'true' if the cell is
 * within the grid boundaries, and 'false' otherwise.
 *
 * Parameters:
 * - row: The row index of the cell.
 * - column: The column index of the cell.
 * - ROWS: The total number of rows in the grid.
 * - COLUMNS: The total number of columns in the grid.
 *
 * Returns:
 * 'true' if the cell is valid, 'false' otherwise.
 */
bool isValidCell(int row, int column, int ROWS, int COLUMNS)
{
    bool isValidRow = row >= 0 && row < ROWS;
    bool isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
}

/*
 * Depth-First Search (DFS) traversal to mark 'O' regions.
 *
 * The 'dfs' function performs a depth-first search starting from a cell at the specified row and
 * column indices in the 'board'. It marks connected 'O' cells as 'U' to indicate they are part of
 * an 'O' region. The function continues the traversal recursively in all valid directions.
 *
 * Parameters:
 * - board: A pointer to a 2D character array representing the board.
 * - row: The current row index.
 * - column: The current column index.
 * - ROWS: The total number of rows in the board.
 * - COLUMNS: The total number of columns in the board.
 */
void dfs(char ***board, int row, int column, int ROWS, int COLUMNS)
{
    if (isValidCell(row, column, ROWS, COLUMNS) == false)
        return;

    if ((*board)[row][column] != 'O')
        return;

    (*board)[row][column] = 'U';

    dfs(board, row - 1, column, ROWS, COLUMNS);
    dfs(board, row + 1, column, ROWS, COLUMNS);
    dfs(board, row, column - 1, ROWS, COLUMNS);
    dfs(board, row, column + 1, ROWS, COLUMNS);
}

/*
 * Solves the surrounded regions on the board.
 *
 * The 'solve' function takes a 2D character array 'board', its size 'boardSize', and an array
 * 'boardColSize' representing the number of columns in each row. It identifies and marks the 'O'
 * regions on the board that are surrounded by 'X'. The 'dfs' function is used to perform depth-first
 * search to mark the 'O' regions.
 *
 * Parameters:
 * - board: A 2D character array representing the board.
 * - boardSize: The number of rows in the board.
 * - boardColSize: An array representing the number of columns in each row of the board.
 */
void solve(char **board, int boardSize, int *boardColSize)
{
    int ROWS = boardSize;
    int COLUMNS = boardColSize[0];

    for (int row = 0; row < ROWS; row++)
        for (int column = 0; column < COLUMNS; column++)
            if (row == 0 || row == ROWS - 1 || column == 0 || column == COLUMNS - 1)
                if (board[row][column] == 'O')
                    dfs(&board, row, column, ROWS, COLUMNS);

    for (int row = 0; row < ROWS; row++)
    {
        for (int column = 0; column < COLUMNS; column++)
        {
            if (board[row][column] == 'O')
                board[row][column] = 'X';

            else if (board[row][column] == 'U')
                board[row][column] = 'O';
        }
    }
}
