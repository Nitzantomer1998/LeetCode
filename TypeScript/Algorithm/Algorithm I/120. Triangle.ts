/**
 * Returns the minimum value between two numbers.
 * @param valueA - The first number.
 * @param valueB - The second number.
 * @returns The minimum value between `valueA` and `valueB`.
 */
function minValue(valueA: number, valueB: number): number { 
    return valueA < valueB ? valueA : valueB;
}

/**
 * Finds the minimum total path sum from the top to the bottom of a triangle.
 * Each step, you may move to adjacent numbers on the row below.
 * @param triangle - A two-dimensional array representing the triangle of numbers.
 * @returns The minimum total path sum.
 */
function minimumTotal(triangle: number[][]): number {
    const triangleHeight: number = triangle.length;

    for (let row: number = triangleHeight - 2; row >= 0; row--) {
        const triangleLength = triangle[row].length;

        for (let column: number = 0; column < triangleLength; column++) {
            const firstOption: number = triangle[row + 1][column];
            const secondOption: number = triangle[row + 1][column + 1];

            triangle[row][column] += minValue(firstOption, secondOption);
        }
    }

    return triangle[0][0];
}
