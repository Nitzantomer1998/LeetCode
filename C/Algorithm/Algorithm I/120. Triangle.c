/* Definition for getting the minimum value */
#define MIN(X, Y) (X < Y ? X : Y)

/*
 * Finds the minimum path sum from the top to the bottom of a triangle of numbers.
 *
 * The 'minimumTotal' function calculates the minimum path sum by iteratively
 * considering two adjacent numbers in each row and selecting the smaller of
 * the two options to add to the current number. This process is repeated
 * for each row from bottom to top until the top of the triangle is reached.
 *
 * Parameters:
 * - triangle: A 2D array representing the triangle of numbers.
 * - triangleSize: The number of rows in the triangle.
 * - triangleColSize: An array containing the number of columns in each row of the triangle.
 *
 * Returns:
 * The minimum path sum from the top to the bottom of the triangle.
 *
 * This function modifies the input 'triangle' array in place, updating each
 * element to store the minimum path sum starting from that element down to
 * the bottom row. It uses a dynamic programming approach to efficiently
 * calculate the minimum path sum.
 *
 * Note: The 'MIN' macro is used to find the minimum of two values.
 */
int minimumTotal(int** triangle, int triangleSize, int* triangleColSize) {
    for (int row = triangleSize - 2; row > -1; row--) {
        for (int column = 0; column < triangleColSize[row]; column++) {
            int leftOption = triangle[row + 1][column];
            int rightOption = triangle[row + 1][column + 1];
            
            triangle[row][column] += MIN(leftOption, rightOption);
        }
    }

    return triangle[0][0];
}
