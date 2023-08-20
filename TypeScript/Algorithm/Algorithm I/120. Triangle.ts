function minValue(valueA: number, valueB: number): number { 
    return valueA < valueB ? valueA : valueB;
}

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
