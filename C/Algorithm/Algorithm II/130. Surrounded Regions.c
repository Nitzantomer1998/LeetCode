#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isValidCell(int row, int column, int ROWS, int COLUMNS)
{
    bool isValidRow = row >= 0 && row < ROWS;
    bool isValidColumn = column >= 0 && column < COLUMNS;

    return isValidRow && isValidColumn;
}

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
