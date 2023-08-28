/**
 * Array of directions for moving in four cardinal directions.
 * Each direction is represented by [row, column] changes.
 */
const directions: [number, number][] = [
    [1, 0],   // Down
    [0, 1],   // Right
    [-1, 0],  // Up
    [0, -1]   // Left
];

/**
 * Checks if a given cell is a valid cell within the matrix.
 * @param {number} matRowSize - The number of rows in the matrix.
 * @param {number} matColumnSize - The number of columns in the matrix.
 * @param {number} row - The row index of the cell.
 * @param {number} column - The column index of the cell.
 * @returns {boolean} Returns true if the cell is within the matrix bounds, otherwise false.
 */
function isValidCell(matRowSize: number, matColumnSize: number, row: number, column: number): boolean {
    return row >= 0 && row < matRowSize && column >= 0 && column < matColumnSize;
}

/**
 * Updates a matrix with distances to the nearest zero element.
 * @param {number[][]} mat - The input matrix of integers.
 * @returns {number[][]} The updated matrix with distances to the nearest zero element.
 */
function updateMatrix(mat: number[][]): number[][] {
    const matRowSize: number = mat.length;
    const matColumnSize: number = mat[0].length;

    const updatedMatrix: typeof mat = Array.from(new Array(matRowSize), () => new Array(matColumnSize));
    const queue: [[number, number], number][] = [];

    for (let row: number = 0; row < matRowSize; row++) {
        for (let column: number = 0; column < matColumnSize; column++) {
            if (mat[row][column] === 0) {
                updatedMatrix[row][column] = 0;
                queue.push([[row, column], 0]);
            } 
            
            else
                updatedMatrix[row][column] = -1;
        }
    }

    while (queue.length > 0) {
        const queueElement = queue.shift();

        if (queueElement) {
            const [[row, column], steps] = queueElement;
            
            for (const [shiftX, shiftY] of directions) {
                const nextRow: number = row + shiftX;
                const nextColumn: number = column + shiftY;

                if (isValidCell(matRowSize, matColumnSize, nextRow, nextColumn)) {
                    if (updatedMatrix[nextRow][nextColumn] === -1) {
                        updatedMatrix[nextRow][nextColumn] = steps + 1;
                        queue.push([[nextRow, nextColumn], steps + 1]);
                    }
                }
            }
        }
    }

    return updatedMatrix;
};
