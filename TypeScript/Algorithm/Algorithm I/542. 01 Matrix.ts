const directions: [number, number][] = [
    [1, 0],   // Down
    [0, 1],   // Right
    [-1, 0],  // Up
    [0, -1]   // Left
];

function isValidCell(matRowSize: number, matColumnSize: number, row: number, column: number): boolean {
    return row >= 0 && row < matRowSize && column >= 0 && column < matColumnSize;
}

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
