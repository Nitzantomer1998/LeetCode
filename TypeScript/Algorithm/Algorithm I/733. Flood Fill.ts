/**
 * Modifies the image by changing the color of connected cells starting from a given cell.
 * @param {number[][]} image - The image represented as a matrix of colors.
 * @param {number} sr - The row index of the starting cell.
 * @param {number} sc - The column index of the starting cell.
 * @param {number} color - The new color to be applied.
 * @returns {number[][]} The modified image with the updated color.
 */
function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
    const ROWS: number = image.length;
    const COLS: number = image[0].length;

    const oldColor: number = image[sr][sc];

    if (oldColor === color)
        return image;

    function dfs(row: number, col: number): void {
        if (row < 0 || col < 0 || row >= ROWS || col >= COLS || image[row][col] !== oldColor)
            return;

        image[row][col] = color;

        dfs(row - 1, col); // Up
        dfs(row + 1, col); // Down
        dfs(row, col - 1); // Left
        dfs(row, col + 1); // Right
    }

    dfs(sr, sc);

    return image;
};
